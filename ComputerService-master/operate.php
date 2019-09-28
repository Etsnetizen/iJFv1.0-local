<?php
    $host=SAE_MYSQL_HOST_M;
    $port=SAE_MYSQL_PORT;
    $user =SAE_MYSQL_USER;
    $pass =SAE_MYSQL_PASS;
    $bdname =SAE_MYSQL_DB;
    session_start();
    $name = $_SESSION['name'];
    if (!$name)
    {
    	echo "<script>alert('您尚未登陆！');window.location.href='login.html'</script>";
    	return false;
    }
	$num=$_GET['aim'];
	date_default_timezone_set("Asia/Shanghai");
	$finish_time = date('Y-m-d H:i:s',time());	//获取当前系统时间
	$con = mysqli_connect($host, $user, $pass, $bdname , $port); 
	if(!$con)
	{
	die('建立连接失败:' . mysqli_connect_error());
	}
	else
	{
		mysqli_query($con,'set names "utf8"'); 
		mysqli_select_db($con,$bdname);  //选择需使用的数据库
		mysqli_query($con,"UPDATE  student SET state = '已处理' WHERE tel='".$num."'");
		mysqli_query($con,"UPDATE  student SET responsible ='$name' WHERE  tel='".$num."'");
		mysqli_query($con,"UPDATE  student SET finish_time ='$finish_time' WHERE  tel='".$num."'");
		echo "<script>alert('操作成功!');window.location.href='finished.php?p=1'</script>";
	}
	mysqli_close($con);
?>