<?php
$servername_con = "localhost";
$username_con = "root";
$password_con = "root";
$dbname_con = "raspberry";
// Crea la conexión
$conn = mysqli_connect($servername_con, $username_con, $password_con,$dbname_con);
// Chequea la conexión
if (!$conn){
    die("Conexión fallida: " . mysqli_connect_error());
}

$sql = "select * from puertas where id=(select max(id) from puertas where puerta='calle') and puerta='calle'";
$result = mysqli_query($conn, $sql);

foreach ($result as $fila) {
	$estado = $fila['estado'];
}
echo "<div>";
	if($estado==0){
		echo "<div style='float:left; width: 230px; text-align: center;'>";
			echo "<img src='puerta_cerrada.jpg'>";
			echo "puerta calle cerrada";
		echo "</div>";
	}else{
		echo "<div style='float:left; width: 230px; text-align: center;'>";
			echo "<img src='puerta_abierta.jpg'>";
			echo "puerta calle abierta";
		echo "</div>";
	}

$sql = "select * from puertas where id=(select max(id) from puertas where puerta='entrada') and puerta='entrada'";
$result = mysqli_query($conn, $sql);

foreach ($result as $fila) {
	$estado = $fila['estado'];
}

	if($estado==0){
		echo "<div style='float:left; width: 230px; text-align: center;'>";
			echo "<img src='puerta_cerrada.jpg'>";
			echo "puerta entrada cerrada";
		echo "</div>";
	}else{
		echo "<div style='float:left; width: 230px; text-align: center;'>";
			echo "<img src='puerta_abierta.jpg'>";
			echo "puerta entrada abierta";
		echo "</div>";
	}
echo "</div>";
?>