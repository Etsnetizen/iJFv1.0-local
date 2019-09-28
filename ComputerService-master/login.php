<?php
    $host=SAE_MYSQL_HOST_M;
    $port=SAE_MYSQL_PORT;
    $user =SAE_MYSQL_USER;
    $pass =SAE_MYSQL_PASS;
    $bdname =SAE_MYSQL_DB;
$inputId = $_POST['Account'];
$inputPass = $_POST['Password'];

$con = mysqli_connect($host, $user, $pass, $bdname , $port); //建立连接
if(!$con)
{
	die('建立连接失败:' . mysqli_connect_error());
}
else
{
	mysqli_query($con,'set names "utf8"'); 
     mysqli_select_db($con,'$bdname');  //选择需使用的数据库
     $stmt = $con->prepare('SELECT * FROM staff WHERE Account = ?');
     $stmt->bind_param('s', $inputId);
     $stmt->execute();
     $result = $stmt->get_result();
    // $result = mysqli_query($con,"SELECT * FROM staff WHERE Account='".$inputId."'");
	//使用mysql_query执行SQL语句
	if($row = mysqli_fetch_array($result)){
		
			if($row['password']!=$inputPass){
				
				echo "<script>alert('密码错误');window.location.href='login.html'</script>";
			    return false;
			}
			else{
				session_start();
				$_SESSION['name']=$row['name'];
				echo "<script>alert('登录成功！正在跳转...')</script>";
                header("Location:unfinished.php?p=1");			
	        }
	}
	else{
		echo "<script>alert('用户不存在');window.location.href='login.html'</script>";
				
				return false;
	}
  }

mysqli_close($con);           //关闭数据库连接
?>