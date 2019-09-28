<?php
    $host=SAE_MYSQL_HOST_M;
    $port=SAE_MYSQL_PORT;
    $user =SAE_MYSQL_USER;
    $pass =SAE_MYSQL_PASS;
    $bdname =SAE_MYSQL_DB;
	$name = $_POST['stu_name']; 
	$stunumber = $_POST['stu_num'];
	$class = $_POST['stu_class'];
	$phone = $_POST['stu_tel'];
	$dorm = $_POST['stu_adr'];
	$discribe = $_POST['stu_desc'];																										
//表单验证
   if (empty($_POST["stu_name"])) {
   echo "<script>alert('提交失败,姓名是必须的！');window.location.href='report.html'</script>";
   return false;
  } 
  if (empty($_POST["stu_num"])) {
  echo "<script>alert('提交失败,学号是必须的！');window.location.href='report.html'</script>";
  return false;
 } 
   if (empty($_POST["stu_class"])) {
   echo "<script>alert('提交失败,班级是必须的！');window.location.href='report.html'</script>";
   return false;
  } 
  if (empty($_POST["stu_adr"])) {
   echo "<script>alert('提交失败,地址是必须的！');window.location.href='report.html'</script>";
    return false;
  } 
  if (empty($_POST["stu_tel"])) {
   echo "<script>alert('提交失败,联系方式是必须的！');window.location.href='report.html'</script>";
    return false;
  } 
  if (empty($_POST["stu_desc"])) {
   echo "<script>alert('提交失败,故障描述是必须的！');window.location.href='report.html'</script>";
    return false;
  } 

    $con = mysqli_connect($host, $user, $pass, $bdname , $port);  //建立连接
    if(!$con)
    {
    	die('建立连接失败:' . mysqli_connect_error());
    }
    else
    {  
    mysqli_query($con,'set names "utf8"'); 
    mysqli_select_db($con,$dbname);  //选择需使用的数据库
	//$result = mysqli_query($con,"SELECT * FROM student WHERE state='未处理' and tel=$phone");
	//$result = mysqli_query($con,"SELECT count(*) FROM student WHERE state='未处理' and tel=$phone");//查询是否有重复的数据
    
    $qid = mysqli_query($con,"SELECT count(*) as total FROM student WHERE state='未处理' and tel=$phone");//查询是否有重复的数据
	$res = mysqli_fetch_array($qid);
	$repeat = $res['total'];
        
	$qid2 = mysqli_query($con,"SELECT count(*) as total FROM(select * from student where to_days(creat_time) = to_days(now()) and state='未处理') as a");//查询是否有重复的数据
	$res2 = mysqli_fetch_array($qid2);
	$todayCount = $res2['total'];
	if($todayCount>=5)
	{	
		 echo "<script>alert('今日表单提交量已达上限，请明天再来啦┭┮﹏┭┮，敬请谅解！ 您也可以添加QQ：2376179548 向我们咨询');window.location.href='index.html'</script>"; 
	}
	else 
	{
		 if($repeat)
	   {
	  	 echo "<script>alert('您已提交过表单，请勿重复提交！');window.location.href='index.html'</script>"; 
	   } 
	     else 
	   { 
	   	$insert=mysqli_query($con,"INSERT INTO student (name,schoolnum,class,tel,adress,description,state) VALUES 
	   	  ('".$name."','".$stunumber."','".$class."','".$phone."','".$dorm."','".$discribe."','未处理')");//使用mysql_query执行SQL语句
       }
	}
	if(!$insert)
    {
    echo "<script>alert('提交失败！');window.location.href='report.html'</script>";
    }
    else
    {
    echo "<script>alert('提交成功！');window.location.href='index.html'</script>";
    }
}
mysqli_close($con);           //关闭数据库连接
?>