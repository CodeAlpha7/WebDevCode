if(window.performance.navigation.type === 1)
{
  document.querySelector(".refresh").innerHTML = ("");
  rolldice();
}

function rolldice()
{
  var randomnumber1 = Math.floor(Math.random() * 6) + 1;
  var randomnumber2 = Math.floor(Math.random() * 6) + 1;

  var randomImageSource = "images/dice" + randomnumber1 + ".png";
  var randomImageSource2 = "images/dice" + randomnumber2 + ".png";

  document.querySelector(".img1").setAttribute("src", randomImageSource);
  document.querySelector(".img2").setAttribute("src", randomImageSource2);

  if(randomnumber1 > randomnumber2)
  {
    document.querySelector("h1").innerHTML = ("Player1 wins!");
  }

  else if (randomnumber2 > randomnumber1)
  {
    document.querySelector("h1").innerHTML = ("Player2 wins!");

  }

  else if (randomnumber1 = randomnumber2)
  {
    document.querySelector("h1").innerHTML = ("Draw!");
  }

}
