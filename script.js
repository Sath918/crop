async function predictCrop(event){

event.preventDefault()

let resultBox = document.getElementById("result")
resultBox.innerHTML = "⏳ Predicting..."

let data = {
N: document.getElementById("N").value,
P: document.getElementById("P").value,
K: document.getElementById("K").value,
temperature: document.getElementById("temperature").value,
humidity: document.getElementById("humidity").value,
ph: document.getElementById("ph").value,
rainfall: document.getElementById("rainfall").value
}

try{

let response = await fetch("http://127.0.0.1:5000/predict",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})

let result = await response.json()

resultBox.innerHTML =
"🌾 Recommended Crop: <b>" + result.recommended_crop + "</b>"

}catch(error){

resultBox.innerHTML =
"⚠️ Server error / API sleeping..."

}

}