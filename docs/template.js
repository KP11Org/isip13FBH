document.addEventListener('DOMContentLoaded', function() {  
    
    var date = new Date();
    console.log(date.toISOString());
    getTasks()
    //createTask("test", date.toISOString())
}, false)

const mockapiURL = "https://67877325c4a42c916106c0c3.mockapi.io/task"
function getTasks(){
    fetch(mockapiURL, {
        method: 'GET',
        headers: {'content-type':'application/json'},
      }).then(res => {
        if (res.ok) {
            return res.json();
        }
        
      }).then(tasks => {
        console.log(tasks);
        
      }).catch(error => {
       
      })
}
function createTask(name, time){
    const newTask = {
        name: name,
        is_complated: false,
        created: time,
      };
      
      fetch(mockapiURL, { method: 'POST',
        headers: {'content-type':'application/json'},
        body: JSON.stringify(newTask)
      }).then(res => {
        if (res.ok) {
            return res.json();
        }
      }).then(task => {
        console.log(task)
      }).catch(error => {
        
      })
}