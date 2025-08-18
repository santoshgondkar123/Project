let input = [... document.querySelectorAll('input')];
console.log(input)
input.forEach(elment =>{
    elment.addEventListener('keyup',()=>{
        if(input.indexOf(elment)+1 != input.length)
            input[input.indexOf(elment)+1].focus()
    
    })
});