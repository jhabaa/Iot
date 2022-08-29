var item = document.querySelector('#temperatureVal')
var humidity = document.querySelector('#humidityVal')
var voltage = document.querySelector('#voltageVal')
var luminosity = document.querySelector('#luminosityVal')
var back = document.querySelector('#vibration')
var container = document.querySelector('#container');
item.innerHTML = "Debut"

var realTemp = 25
function GetrealVoutTemp(){
    Vt = 870.6 - (5.506 * (realTemp - 30)) - (0.00176 * (realTemp - 30)^2)
    return Vt
}

//function to get luminosity in lux
function GetLuminosity(e){
  i = e/5500;
  return ( i * 1000000).toFixed(2);
}
// function to get Humidity
var humidityTable =[
  [0,0,5,10,15,20,25,30,35,40,45,50],
  [20,0,0,0,21000,13500,9800,8000,6300,4600,3800,3200],
  [25,0,19800,16000,10500,6700,4803,3900,3100,2300,1850,1550],
  [30,12000, 980, 7200, 5100, 3300, 2500, 2000, 1500, 1100, 900, 750],
  [35,5200, 4700, 3200, 2350, 1800, 1300, 980, 750, 575, 430, 350],
  [40,2800, 2000, 1400, 1050, 840, 630, 470, 385, 282, 210, 170],
  [45,720, 510, 386, 287, 216, 166, 131, 104, 80, 66, 51],
  [50,384, 271, 211, 159, 123, 95, 77, 63, 52, 45, 38],
  [55,200, 149, 118, 91, 70, 55, 44, 38, 32, 30, 24],
  [60,108, 82, 64, 51, 40, 31, 25, 21, 17, 14, 12],
  [65,64, 48, 38, 31, 25, 20, 17, 13, 11, 9, 8],
  [70,38, 29, 24, 19, 16, 13, 10.5, 9, 8.2, 7.1, 6.0]
]
function GetHumidity(Vm, Vin, temperature){
  //rh = (((3.3*47000)-(Vm * 47000))/Vm)
  //r = getMinusInHumidityTable(25,rh);
  rh = ((Vin * 100)/Vm) - 100;
  console.log(humidityTable[0]);
  r = getMinusInHumidityTable(temperature,rh);
  return r
}
function getMinusInHumidityTable(t, rh){

  // We are looking for the right temperature in the first line
  temp = Math.round(t);
  rh = Math.round(rh);
  console.error("RH est de  : " +rh);
  console.error("T est de  : " +temp);
  if (humidityTable[0].indexOf(temp)){
  
  }else{
    do {
      temp ++;
    } while (!humidityTable[0].indexOf(temp));
  }
 
  //console.log(temp);

  // Get the rh coord
  val = 100000;
  indexY = 1;
  for(b =0; b< humidityTable.length; b++){
    for (a = 0; a<humidityTable[b].length ;a++){
      //console.error(humidityTable[b][a]);
        val = Math.abs(humidityTable[b][a]-rh) < val ? humidityTable[b][a] : val;
        indexY = Math.abs(humidityTable[b][a]-rh) < val ? b : indexY;
    }
  }
  console.error("on garde la position Y : " +indexY);

  return humidityTable[indexY][humidityTable[0].indexOf(temp)];

}
//here are codes for graphs 
temps = []
luminosities = []
humidities = []
voltages = []
var lab = []
for (var i =0; i<50;i++){
  lab.push(i.toString())
}
const dataTemp = {
  labels: lab,
  datasets: [{
    label: 'temperature',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    cubicInterpolationMode:"monotone",
    data: temps,
    radius:0,
    stepped: true,
  }]
};
const dataHum = {
  labels: lab,
  datasets: [{
    label: 'Humidity',
    backgroundColor: 'rgb(0, 0, 0)',
    borderColor: 'rgb(0, 0, 250)',
    cubicInterpolationMode:"monotone",
    data: humidities,
  }]
};
const dataLum = {
  labels: lab,
  datasets: [{
    label: 'Luminosity',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    cubicInterpolationMode:"monotone",
    data: luminosities,
  }]
};
const dataVol = {
  labels: lab,
  datasets: [{
    label: 'Voltages',
    backgroundColor: 'rgb(255, 0, 0)',
    borderColor: 'rgb(255, 0, 0)',
    cubicInterpolationMode:"monotone",
    data: voltages,
    stepped: true,
    radius:0,
  }]
};

var tempChar = new Chart(document.querySelector("#tempChart"), {
  type:'line',
  data:dataTemp,
  options:{
  animation:false,
 
  }
});
var humChar = new Chart(document.querySelector("#humChart"), {
  type:'line',
  data:dataHum,
  options:{}
});
var lumChar = new Chart(document.querySelector("#lumChart"), {
  type:'line',
  data:dataLum,
  options:{}
});
var volChar = new Chart(document.querySelector("#volChart"), {
  type:'line',
  data:dataVol,
  options:{}
});

//When we got a message
socket.on('my message', function(msg) {
    vibrationSensor = msg["Vibration"].toFixed(2);
    item.innerHTML = TemperatureFormula(msg["Temperature"]).toFixed(2);
    humidity.innerHTML = GetHumidity(msg["Voltage"],msg["Humidity"],TemperatureFormula(msg["Temperature"]));
    voltage.innerHTML = msg["Voltage"].toFixed(2);
    luminosity.innerHTML = GetLuminosity(msg["Luminosity"]);
    temps.unshift(TemperatureFormula( msg["Temperature"]).toString())
    humidities.unshift(GetHumidity(msg["Humidity"]));
    luminosities.unshift(GetLuminosity(msg["Luminosity"]));
    voltages.unshift(msg["Voltage"]);
    humChar.update();
    lumChar.update();
    volChar.update();
    tempChar.update();
    //messages.appendChild(item);
    //window.scrollTo(0, document.body.scrollHeight);

    //Animations
    if(GetLuminosity(msg["Luminosity"])){
        anime({
          targets: '.vibration',
          opacity:GetLuminosity(msg["Luminosity"])/600,
          duration: 1000,
          easing: 'easeInOutQuart'
        });
        if (GetLuminosity(msg["Luminosity"]) <100){
          document.getElementById("container").style.color = 'black';
          document.querySelectorAll(".card").forEach((item)=>{
            item.style.color = 'black';
        })
        }else{
          document.getElementById("container").style.color = 'whitesmoke';
          document.querySelectorAll(".card").forEach((item)=>{
              item.style.color = 'whitesmoke';
          })
          
        }
    }
    if (vibrationSensor > 1){
      anime({
        targets:'.cards',
        translateX:"250px",
        translateY:"100px"
      })
    }else{
      anime({
        targets:'.cards',
        translateX:"0px",
        translateY:"0px"
      })
    }
    
});

  //Background
  VANTA.GLOBE({
    el: "#body",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    color: 0x6bff,
    color2: 0x0,
    size: 1.90,
    backgroundColor: 0xffffff
  })

function TemperatureFormula(Vtemp){
    console.log(Vtemp);
    a = Math.sqrt(Math.pow(-5.506,2) + (4*0.00176*(870.6-Vtemp)));
    b = 2*(-0.00176)
    //console.log(a);
    //console.log(b);
    t = ((5.506 - a)/b) + 27
    return t 
}


//console.log("real temperature : " + GetrealVoutTemp())

