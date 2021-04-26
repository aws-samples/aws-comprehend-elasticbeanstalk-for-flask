import os
import time
import boto3
import pandas as pd
from collections import Counter

start_time = time.time()
comprehend = boto3.client("comprehend", region_name='us-east-1')
accepted_entities = ['EVENT', 'LOCATION', 'ORGANIZATION', 'PERSON', 'COMMERCIAL_ITEM']
# skipping DATE, OTHER, QUANTITY as they don't make sense in this context

def process_csv_file(file_path, max_rows=50):
    if os.path.splitext(file_path)[1] != '.csv':
        print("Wrong input format, only CSV files supported. \nExiting.")
        return
    print("Reading input file...")
    input_df = pd.read_csv(file_path, nrows=max_rows)
    if input_df.shape[1] > 1:
        print("Input format is wrong. Please input a file with single column containing tweets/text.\nExiting.")
        return
    input_df.columns = ["Text"]
    text_list = list(input_df.Text.values)
    
    sentiments = []
    entities = []
    
    for i in range(0, len(text_list), 20):  #batch accepts ony 25 docs at a time
        start = i
        end = min(i+19, len(text_list))
        response = comprehend.batch_detect_sentiment(
            LanguageCode="en",
            TextList=text_list[start: end]
            )
        sentiments.extend([result['Sentiment'] for result in response['ResultList']])
        
        response_ent = comprehend.batch_detect_entities(
            LanguageCode="en",
            TextList=text_list[start: end]
            )
        for ent in response_ent['ResultList']:
            if ent['Entities']:  # entities detected
                for e in ent['Entities']:
                    if e['Type'] in accepted_entities:
                        if (len(e['Text']) > 2) and not (str(e['Text']).replace('@', '').isdecimal()):
                            entities.append(
                                [e['Text'], e['Type']]
                                )

    sentiment_counts = Counter(sentiments)
    # entities has both type and text if you like!
    top_ents = Counter([ent[0] for ent in entities]).most_common(15)
    print("Time taken: ", time.time() - start_time)
    # print(results)
    data_output = {
        "entity": 
        {
            "label": [x for (x,y) in top_ents],
            "count": [y for (x,y) in top_ents]
        },
        "sentiment":
        {
            "label": list(sentiment_counts.keys()),
            "count": list(sentiment_counts.values())
        }
    }
    # print(data_output)
    return data_output
    
if __name__ == "__main__":
    process_csv_file("sampleData/sample_tweets.csv")