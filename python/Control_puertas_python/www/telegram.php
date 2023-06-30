<?php
$servername_con = "localhost";
$username_con = "root";
$password_con = "root";
$dbname_con = "raspberry";

$conn = mysqli_connect($servername_con, $username_con, $password_con,$dbname_con);
if (!$conn){
	die("Conexión fallida: " . mysqli_connect_error());
}

$hoy = getdate();
$num_dia_semana = $hoy["wday"];
$num_dia_mes = $hoy["mday"];
$num_mes = $hoy["mon"];
$num_anno = $hoy["year"];

$fecha_hoy=$num_anno."-".$num_mes."-".$num_dia_mes;

$sql = "select * from dias_alarma where tipo='fin_de'";
$result = mysqli_query($conn, $sql);

foreach ($result as $fila) {
	$num_dias = $fila['num_dia'];
	$activo = $fila['activo'];
}

if($activo == 1){
	$checked="checked";
	if($num_dia_semana == 5 or $num_dia_semana == 6){
		$token = "xxxxxxxxxxx";
		$id = "xxxxxxxx";
		$urlMsg = "https://api.telegram.org/bot{$token}/sendMessage";
		$msg = "Mensaje de fin de semana";
		 
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $urlMsg);
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, "chat_id={$id}&parse_mode=HTML&text=$msg");
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

		$server_output = curl_exec($ch);
		$server_output_true = strpos($server_output, "true");
		$server_output_false = strpos($server_output, "false");

		if($server_output_true !== false){
			echo "Envio correcto";
		}
		if($server_output_false !== false){
			echo "Error envio";
		}
		curl_close($ch);
	}
}else{
	$checked="";
}
$sql = "select * from dias_alarma where tipo='dia' and fecha='$fecha_hoy'";
$result = mysqli_query($conn, $sql);

foreach ($result as $fila) {
	$fecha = $fila['fecha'];
	$activo = $fila['activo'];
	
	$token = "xxxxxxxxxxxxxx";
	$id = "xxxxxxxxxxx";
	$urlMsg = "https://api.telegram.org/bot{$token}/sendMessage";
	$msg = "Mensaje dia especifico";
	 
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $urlMsg);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, "chat_id={$id}&parse_mode=HTML&text=$msg");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

	$server_output = curl_exec($ch);
	$server_output_true = strpos($server_output, "true");
	$server_output_false = strpos($server_output, "false");

	if($server_output_true !== false){
		echo "Envio correcto";
	}
	if($server_output_false !== false){
		echo "Error envio";
	}
	curl_close($ch);
}
?>