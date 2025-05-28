let text = ""

window.onload = () =>{
    animateBar();

    setInterval(()=>{
        if( text == document.getElementById("input-text").value)
            return;
      
        text = document.getElementById("input-text").value
        fetch("/predict",{
            method:"POST",
            headers: { 'Content-Type': 'application/json' },
            body:JSON.stringify({text})
        })
        .then(res=>res.json())
        .then(data=>{
            animateBar(data.probability);
        });
    },250);

}


/**
 * Anima la barra di avanzamento
 * 
 * @param {Number} prob
 */
function animateBar(prob = 0.5) {
    let percentage = Math.round(prob * 100);

    let r = Math.round(255 * (1 - prob));
    let g = Math.round(128 * prob);
    let color = `rgb(${r}, ${g}, 0`;

    let bar = document.getElementById("bar")
    bar.style.width = `${percentage}%`;
    bar.style.backgroundColor = color;
    bar.textContent = `${percentage}%`;
}
