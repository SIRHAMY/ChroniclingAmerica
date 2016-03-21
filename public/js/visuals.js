
d3.csv("./resources/housewifeRes1000.csv", function(error, data) {

  //**Frequency Bar Chart**
  var graphX1 = [];
  var graphY1 = [];

  var graphNeg = [];
  var graphYear =[];

  data.forEach(function(d) {
    graphX1.push(d.year);
    graphY1.push(d.pos);
    graphYear.push(d.year);
    graphNeg.push(d.neg);
    console.log(d);
  })
  /*
  for(i in data) {
    console.log(i);
    graphX.push(i[0]);
    graphY.push(i[1]);
  }
  */

  var layout1 = {
    title: 'Positive Article Count',
    barmode: 'stack',
    xaxis: {
      title: 'Year'
    },
    yaxis: {
      title: 'Positive Articles'
    }
  }

  var Graph1Trace1 ={
      x: graphX1,
      y: graphY1,
      name: 'Positive',
      type:'bar'
    };

  var Graph1Trace2 = {
    x: graphYear,
    y: graphNeg,
    name: 'Negative',
    type: 'bar',
    marker: {
      color: 'rgb(255,92,92)'
    }
  };

  var myGraph1 = [Graph1Trace1, Graph1Trace2];

  Plotly.newPlot('Frequency', myGraph1, layout1);

  //**Percentage Bar Chart**
  var graphX2 = [];
  var graphY2 = [];

  data.forEach(function(d) {
    graphX2.push(d.year);
    graphY2.push( parseInt(d.pos) * 1.0 / (parseInt(d.pos) + parseInt(d.neg) ) );
  });

  var layout2 = {
    title: 'Percentage Articles Positive',
    xaxis: {
      title: 'Year'
    },
    yaxis: {
      title: 'Percentage Positive'
    }
  }

  var myGraph2 =[{
      x: graphX2,
      y: graphY2,
      type:'bar'
    }
  ];

  Plotly.newPlot('Percentage', myGraph2, layout2);

});

/*
function type(d) {
  d.frequency = +d.frequency;
  return d;
}*/