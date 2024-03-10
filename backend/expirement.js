
const {spawn}=require("child_process");
const { send } = require("process");


Ytlink="https://www.youtube.com/watch?v=TmVqwhBUiSM"
ytid=Ytlink.split("=")[1]
ytembed=`https://www.youtube.com/embed/${ytid.slice(0,11)}`
console.log(Ytlink)
console.log(typeof(Ytlink))
console.log(ytembed)
console.log("request 1 ")
const child= spawn("python",['sample.py',Ytlink]);
child.stdout.on('data',(data)=>{
   
    data1= data.toString()
    console.log(data1)
    console.log("request recived ")
    data33={
        link:ytembed,
        data:data1
    }
    //setTimeout()
})