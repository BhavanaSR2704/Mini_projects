function selectCategory(cat){

localStorage.setItem(
"category",
cat
);

window.location=
"expense.html";

}



window.onload=function(){

let cat=
localStorage.getItem(
"category"
);

let x=
document.getElementById(
"category"
);

if(x){

x.innerHTML=
"Selected : "+cat;

}

}



function saveExpense(){

let name=
document.getElementById(
"name"
).value;

let amount=
document.getElementById(
"amount"
).value;

let category=
localStorage.getItem(
"category"
);


if(name==""||amount==""){

alert(
"Enter all fields"
);

return;

}


let data={

name:name,

amount:Number(amount),

category:category

};


localStorage.setItem(

"latestExpense",

JSON.stringify(data)

);


window.location=
"report.html";

}



function showReport(){


let data=

JSON.parse(

localStorage.getItem(
"latestExpense"
)

);


if(data==null){

document.getElementById(
"result"
).innerHTML=

"<h2 style='color:white'>No expense added</h2>";

return;

}


document.getElementById(
"result"
).innerHTML=

`

<div class='card'>

<h2>
Today's Expense
</h2>

<h1>
₹${data.amount}
</h1>

<h3>
${data.category}
</h3>

<p>
${data.name}
</p>

</div>

`;

}
