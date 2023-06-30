<html>
<header>
<script type="text/javascript" language="javascript">
function refreshDivs(divid,secs,url)
{

	// define our vars
	var divid,secs,url,fetch_unix_timestamp;

	// Chequeamos que las variables no esten vacias..
	if(divid == ""){ alert('Error: escribe el id del div que quieres refrescar'); return;}
	else if(!document.getElementById(divid)){ alert('Error: el Div ID selectionado no esta definido: '+divid); return;}
	else if(secs == ""){ alert('Error: indica la cantidad de segundos que quieres que el div se refresque'); return;}
	else if(url == ""){ alert('Error: la URL del documento que quieres cargar en el div no puede estar vacia.'); return;}

	// The XMLHttpRequest object

	var xmlHttp;
	try{
		xmlHttp=new XMLHttpRequest(); // Firefox, Opera 8.0+, Safari
	}
	catch (e){
		try{
			xmlHttp=new ActiveXObject("Msxml2.XMLHTTP"); // Internet Explorer
		}
		catch (e){
			try{
				xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch (e){
				alert("Tu explorador no soporta AJAX.");
				return false;
			}
		}
	}

	// Timestamp para evitar que se cachee el array GET

	fetch_unix_timestamp = function()
	{
		return parseInt(new Date().getTime().toString().substring(0, 10))
	}

	var timestamp = fetch_unix_timestamp();
	var nocacheurl = url+"?t="+timestamp;

	// the ajax call
	xmlHttp.onreadystatechange=function(){
		if(xmlHttp.readyState == 4 && xmlHttp.status == 200){
			document.getElementById(divid).innerHTML=xmlHttp.responseText;
			setTimeout(function(){refreshDivs(divid,secs,url);},secs*1000);
		}
	}
	xmlHttp.open("GET",nocacheurl,true);
	xmlHttp.send(null);
}

// LLamamos las funciones con los repectivos parametros de los DIVs que queremos refrescar.
window.onload = function startrefresh(){
	refreshDivs('estado_puerta',1,'consulta.php');
}
</script>


</header>
	<body>
		<div id="estado_puerta">
		
		
		</div>
	</body>
</html>