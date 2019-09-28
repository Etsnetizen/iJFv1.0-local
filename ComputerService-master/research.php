<?php
	$host=SAE_MYSQL_HOST_M;
	$port=SAE_MYSQL_PORT;
	$user =SAE_MYSQL_USER;
	$pass =SAE_MYSQL_PASS;
	$bdname =SAE_MYSQL_DB;
	$phone=$_POST['stu_tel'];
	$con = mysqli_connect($host, $user, $pass, $bdname , $port);  //建立连接
	if(!$con)
	{
	die('建立连接失败:' . mysqli_connect_error());
	}
	else
	{
		mysqli_query($con,'set names "utf8"'); 
		mysqli_select_db($con,$bdname);  //选择需使用的数据库
		 $qid = mysqli_query($con,"SELECT count(*) as total FROM student WHERE state='未处理' and tel = $phone");//查询是有该电话对应的数据
	     $res = mysqli_fetch_array($qid);
	     $exit = $res['total'];
		
        $qid_2 = mysqli_query($con,"SELECT rownum from (select @rownum:=@rownum+1 AS rownum,number,state,tel from `student`,(SELECT @rownum:=0) r ORDER BY state,number)b  WHERE tel = $phone "); //该电话对应的行数在未完成记录中是多少 
        $res_2 = mysqli_fetch_array($qid_2);
		$r = $res_2['rownum'];
		
        
		$qid_3 = mysqli_query($con,"SELECT count(*) as total FROM student WHERE state='已处理'");
		$res_3 = mysqli_fetch_array($qid_3);
		$done = $res_3['total']; //已完成的数量
        echo"$done";
            
		if($exit)
		{   
			if(($r-$done)==1)
			{
				echo"<script>alert('你是第一个,修机小部队会马上和你联系,请耐心等待┗|｀O′|┛ 嗷~~');window.location.href='index.html'</script>";
			}
				
			else if(($r-$done)>1)
			{
		        echo"<script>alert('当前排队等待人数 ".($r-$done).",修机小部队正努力向你飞驰,请耐心等待噢┗|｀O′|┛ 嗷~~');window.location.href='index.html'</script>";
			 }
		} 
		else echo"<script>alert('暂无数据');window.location.href='index.html'</script>";
    }
	mysqli_close($con);
?>