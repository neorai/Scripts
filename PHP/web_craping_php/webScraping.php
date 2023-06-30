<?php 
$result = file_get_contents("http://bo.cope.webtv.flumotion.com/api/active?format=json&podId=78");
$array_full=(json_decode($result, true));

$symbols = array('"','}','{','image','author','title',',');
$array_full['value'] = str_replace($symbols, "", $array_full['value']);



$array_author_title= explode(": ", $array_full['value']);
$array_author_title[2] = str_replace($symbols, "", $array_author_title['2']);
$array_author_title[3] = str_replace($symbols, "", $array_author_title['3']);


echo "Author: ".$array_author_title[2];
echo "</br>Title: ".$array_author_title[3];	
?>
