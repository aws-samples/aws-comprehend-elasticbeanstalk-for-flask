## Visualize AI/ML Model Results using Flask and AWS Elastic Beanstalk

The contents of this repository provide a example Flask application that passes user-provided data to Amazon Comprehend and visualizes the results using Plotly. The steps below also demonstrate how to deploy this application to Amazon Elastic Beanstalk.

**NOTE:** This repository is designed to supplement an APG library guide, content for the guide can be viewed in Quip
[here](https://quip-amazon.com/oDV5AclxbSXv/Comprehend-Flask-APG).

### Steps to implement the application:
1. Sign in to an AWS account with administrator privileges.
2. Clone this repository into your working machine.
3. cd into the repository and install the requirements using
`pip install -r requirements.txt`
4. Test the Flask application locally, using `python application.py`
This should return information about serving the application, with an output similar to the below - 
```
* Serving Flask app "application" (lazy loading) 
* Environment: production
 WARNING: This is a development server. Do not use it in a production deployment.
 Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
You can now access the app using the URL in your output.


### Deploy the application to AWS Elastic Beanstalk

5. Initialize your AWS Elastic Beanstalk application using 
`eb init -p python-3.6 <app-name> --region <region_name>`
6. Create and deploy the Elastic Beanstalk environment using `eb create <env-name>`
7. Make sure to add Amazon Comprehend access to the EC2 instance created using AWS Elastic Beanstalk. You can use either
the AWS console or use the command below.
`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/ComprehendFullAccess --role-name aws-elasticbeanstalk-ec2-role`

This will begin the provisioning all of the necessary architectural components within AWS. 
This process can take about 5 minutes to complete. Once your application is successfully deployed, 
the deployment URL should be returned in the command line, or you can run `eb open` to open 
your application in the browser.

## Credits and References:

- [Plotly Documentation](https://plotly.com/javascript/)

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

