<?php
    $host=SAE_MYSQL_HOST_M;
    $port=SAE_MYSQL_PORT;
    $user =SAE_MYSQL_USER;
    $pass =SAE_MYSQL_PASS;
    $bdname =SAE_MYSQL_DB;
	$name = $_POST['tea_name']; 
	$phone = $_POST['tea_tel'];
	$adress = $_POST['tea_adr'];
	$describe = $_POST['tea_desc'];	
if (empty($_POST["tea_name"])) {
   echo "<script>alert('提交失败,姓名是必须的！');window.location.href='report.html'</script>";
   return false;
  } 
   if (empty($_POST["tea_tel"])) {
   echo "<script>alert('提交失败,联系方式是必须的！');window.location.href='report.html'</script>";
   return false;
  } 
  if (empty($_POST["tea_adr"])) {
   echo "<script>alert('提交失败,地址是必须的！');window.location.href='report.html'</script>";
    return false;
  } 
  if (empty($_POST["tea_desc"])) {
   echo "<script>alert('提交失败,简要描述是必须的！');window.location.href='report.html'</script>";
    return false;
  } 
$con = mysqli_connect($host, $user, $pass, $bdname , $port); //建立连接
if(!$con)
{
	die('建立连接失败:' . mysqli_connect_error());
}
else
{  
	mysqli_query($con,'set names "utf8"'); 
    mysqli_select_db($con,$bdname);  //选择需使用的数据库
     $insert=mysqli_query($con,"INSERT INTO teacher (name,tel,adress,description,state) VALUES ('".$name."','".$phone."','".$adress."','".$describe."','未处理')");//使用mysql_query执行SQL语句
	 if(!$insert){
   echo "<script>alert('提交失败');window.location.href='report.html'</script>";
 }else{
   echo "<script>alert('提交成功！');window.location.href='index.html'</script>";
 }
}
mysqli_close($con);           //关闭数据库连接
?>