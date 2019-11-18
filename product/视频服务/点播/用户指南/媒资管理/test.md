<!DOCTYPE html>  
<html>  
<head>  
<meta charset="utf-8">  
<title>test</title>  
<script type="text/javascript">
	window.onload=function(){
		window.alert(screen.width)
	if (screen.width <= 450){
		console.log("<=450")
  		var img = new Image()
		img.src="img/111.png"
		img.width="1000"
		img.useMap = "#map2"
		var div = document.getElementById('d1')
		img.onload = function() {
			div.appendChild(img)
		}
          }else {
          		console.log(">450")
          		var img = new Image()
				img.src="img/111.png"
				img.width="1800"
				img.useMap = "#map"
				var div = document.getElementById('d1')
				img.onload = function() {
					div.appendChild(img)
				}
      	}
}
</script>
</head>  

<body>  
	<div id = "d1">
	<map name="map" >  
	  <area  shape="rect" coords="133,2734,427,2860"  href="http://www.douyu.com" onfocus="blur(this)" >  
	</map>  
	<map name="map2" >  
	  <area  shape="rect" coords="89,1535,209,1575"  href="http://www.douyu.com" onfocus="blur(this)" >  
	</map> 
</body>  

</html> 
