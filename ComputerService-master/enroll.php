<?php
    $host=SAE_MYSQL_HOST_M;
    $port=SAE_MYSQL_PORT;
    $user =SAE_MYSQL_USER;
    $pass =SAE_MYSQL_PASS;
    $bdname =SAE_MYSQL_DB;
$inputId = $_POST['Account'];
$inputPass = $_POST['Password'];


	$name = $_POST['name']; 
	$sex = $_POST['sex'];
	$class = $_POST['class'];
	$college = $_POST['college'];
	$add = $_POST['address'];
	$tel = $_POST['tel'];
	$self = $_POST['self'];
	$join = $_POST['join'];
/*if (empty($_POST["name"])) {
   echo "<script>alert('提交失败,姓名是必须的！');window.location.href='enroll.html'</script>";
   return false;
  } 
  if (empty($_POST["sex"])) {
   echo "<script>alert('提交失败,性别是必须的！');window.location.href='enroll.html'</script>";
    return false;
  } 
  if (empty($_POST["class"])) {
   echo "<script>alert('提交失败,班级是必须的！');window.location.href='enroll.html'</script>";
    return false;
  } 
  if (empty($_POST["college"])) {
   echo "<script>alert('提交失败,学院是必须的！');window.location.href='enroll.html'</script>";
    return false;
  } 
 if (empty($_POST["address"])) {
   echo "<script>alert('提交失败,具体地址是必须的！');window.location.href='enroll.html'</script>";
    return false;
  } 
 if (empty($_POST["self"])) {
   echo "<script>alert('提交失败,自我介绍是必须的！');window.location.href='enroll.html'</script>";
    return false;
  }
if (empty($_POST["jion"])) {
   echo "<script>alert('提交失败,对我们的期望是必须的！');window.location.href='enroll.html'</script>";
    return false;
  }*/
	$con = mysqli_connect($host, $user, $pass, $bdname,$port); //建立连接																										
if(!$con)
{
	die('建立连接失败:' . mysqli_connect_error());
}
else
{  
	mysqli_query($con,'set names "utf8"'); 
    mysqli_select_db($con,$bdname);  //选择需使用的数据库
		$total_sql="SELECT COUNT(*)FROM enroll where tel=$tel";
		$total_result=mysqli_fetch_array(mysqli_query($con,$total_sql));
		$total=$total_result[0];
 	if($total>0)
	   echo "<script>alert('您已提交过报名表，请勿重复提交！');window.location.href='index.html'</script>"; 
	else 
	   $insert=mysqli_query($con,"INSERT INTO enroll (name,sex,class,college,address,tel,self,jointext) 
	   VALUES ('".$name."','".$sex."','".$class."','".$college."','".$add."','".$tel."','".$self."','".$join."')");
		//使用mysql_query执行SQL语句
    if(!$insert)
    {
    echo "<script>alert('提交失败！');window.location.href='enroll.html'</script>";
    }
    else
    {
    echo "<script>alert('提交成功！');window.location.href='index.html'</script>";
    }
}
mysqli_close($con);           //关闭数据库连接
?>