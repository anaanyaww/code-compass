import React, { useState } from 'react';
import axios from "axios";
import {Link} from "react-router-dom";
const ChatBox = () => {
    const[stack,setStack]= useState(["Hello ! Ask me a question?"])
    const[usermessage,setUser]=useState("")
    const response=()=>{
        setStack([...stack,usermessage])
        axios.post("/chatresponse",{
            ques:usermessage
        })
        .then((response)=>{
            console.log(response.data.anaylsis)
            setStack([...stack,response.data.anaylsis])
        })
       
    }
    const sendmessage=()=>{
        setStack([...stack,usermessage])
    }
    const updatedata=(event)=>{
        setUser(event.target.value)
    }

 return(
    <div>
   
  
        <h1>Neil tells </h1>
    <textarea
                style={{ width: '344px', height: '500px' }}
                value={stack.map((message)=>{
                   return message+"\n\n"
                })}
                placeholder="Neil tells ..."
                readOnly
            />
    <br></br>
    <input  type="text" onChange={updatedata}/>
     <button  onClick={response}>Send!</button>
    
            
     </div>
    
 )
};




export default ChatBox;