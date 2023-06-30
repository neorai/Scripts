<html>
	<head>
		<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
		<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
		<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
		<script src="datepicker-es.js"></script>
		<script>
		$(function () {
			$( "#datepicker" ).datepicker();
			$( "#datepicker" ).datepicker( "option", "dateFormat", "dd-mm-yy" );
			$( "#datepicker" ).datepicker( $.datepicker.regional[ "es" ] );
		});
		</script>
	</head>
<body>
	<?php
	$servername_con = "localhost";
	$username_con = "root";
	$password_con = "root";
	$dbname_con = "raspberry";
	$conn = mysqli_connect($servername_con, $username_con, $password_con,$dbname_con);
	if (!$conn){
		die("Conexión fallida: " . mysqli_connect_error());
	}

	if(isset($_REQUEST['datepicker'])){
		$datepicker = $_REQUEST['datepicker'];
		$datepicker = date("Y-m-d", strtotime($datepicker));
		$sql = "INSERT INTO dias_alarma (tipo, fecha, activo)
				VALUES ('dia', '$datepicker', '1'); ";
		echo $sql;
		$result = mysqli_query($conn, $sql);
	}

	if(isset($_REQUEST['fin_de'])){
		$value_fin_de=$_REQUEST['fin_de'];
		if($value_fin_de == 0){
			$sql = "UPDATE dias_alarma
					SET activo = 1
					WHERE tipo='fin_de'";
			$result = mysqli_query($conn, $sql);
		}
	}else{
		$sql = "UPDATE dias_alarma
				SET activo = 0
				WHERE tipo='fin_de'";
		$result = mysqli_query($conn, $sql);
	}

	$hoy = getdate();
	//var_dump($hoy);

	/*if ($hoy["weekday"]=="Monday") $dia="Lunes";
	if ($hoy["weekday"]=="Tuesday") $dia="Martes";
	if ($hoy["weekday"]=="Wednesday") $dia="Miércoles";
	if ($hoy["weekday"]=="Thursday") $dia="Jueves";
	if ($hoy["weekday"]=="Friday") $dia="Viernes";
	if ($hoy["weekday"]=="Saturday") $dia="Sabado";
	if ($hoy["weekday"]=="Sunday") $dia="Domingo";
	*/
	
	$num_dia_semana = $hoy["wday"];
	$num_dia_mes = $hoy["mday"];
	$num_mes = $hoy["mon"];
	$num_anno = $hoy["year"];

	$fecha_hoy=$num_anno."-".$num_mes."-".$num_dia_mes;

	echo $fecha_hoy;

	$sql = "select * from dias_alarma where tipo='fin_de'";
	$result = mysqli_query($conn, $sql);

	foreach ($result as $fila) {
		$num_dias = $fila['num_dia'];
		$activo = $fila['activo'];
	}

	if($activo == 1){
		$checked="checked";
		
	}else{
		$checked="";
	}

	echo "<form action='#' method='post'>";
			echo "<input type='checkbox' name='fin_de' value='$activo' $checked>Los fines de semana<br>";
			echo "<input type='text' name='datepicker' id='datepicker'><br>";
			echo "<input type='submit' name='enviar' value='Enviar'>";

	echo "</form>";


	?>
</body>
<html>