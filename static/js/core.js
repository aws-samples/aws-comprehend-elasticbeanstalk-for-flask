var buildChart = function (data, divID) {
    // Bar Chart visual using Plotly

    // Gather data for plot
    var data = [
        {
            x: data.label,
            y: data.count,
            type: 'bar'
        }
    ];

    // customize chart layout
    var layout = {
        xaxis: {
            automargin: true
        }
    };

    // Create the plot at the given div ID
    Plotly.newPlot(divID, data, layout);

};


var buildCharts = function () {

    // get data output from Flask's /data route
    d3.json('data').then(data => {

        // Construct visuals
        buildChart(data.entity, "EntityChart")
        buildChart(data.sentiment, "SentimentChart");

        // remove loading gif once plots are ready
        document.getElementById("loading").style.display = 'none';
        document.getElementById("loading-image").style.display = 'none';

    }
    )
};

buildCharts();