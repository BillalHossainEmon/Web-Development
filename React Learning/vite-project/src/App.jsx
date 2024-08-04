import React from 'react';

const App = () => {
    let marks = 80;
    const city=['Dhaka', 'London', 'Delhi', 'Kolkata']
    return (
   //Short Hand If Else
    
    //     <div>
    //         {
    //         marks > 80 ?
    //         <h1>Brilliant Result</h1>
    //         :
    //         <h1>Average Result</h1>
    //         }
    //     </div>
    

    //Imidiately Invoked Functions IIF
      <div>
        {(() =>{
            
            if(marks>80 && marks<100){
              return <h1>Brilliant Result</h1>;
            }
            else if(marks>=60 && marks<=80){
              return <h1>Average Result</h1>;
            }

          })()}

        <ul>
          {
            city.map((item,i)=>{
              return <li key={i.toString()}>{item}</li>
            })
          }
        </ul>
      </div>
    )
}

export default App;
