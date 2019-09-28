<?php session_start();
$name=$_SESSION['name'];
if(!$name){
   echo"<script>alert('您尚未登陆！');window.location.href='login.html'</script>";
   return false;
}
    
?> 
<!DOCTYPE HTML>
<html lang="en">
<head>
	<title>广药计服</title>
	<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" href="image/">
	<link rel="stylesheet" type="text/css" href="css/index.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<script type="text/javascript" src="js/jquery-3.3.1.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
     <style>	 
    		 nav.pagination{width:75%;margin:0 auto;margin-top: 50px;}
    		 ul.pagination{width:auto;margin:0 auto;}
    		 form{
    		     display: inline;
    		 }
    </style>
	</head>
<body>
	<!-- 导航栏 -->
<nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light"> <a class="navbar-brand" href=""><img src="image/logo2.png" alt="logo" width="250px" height="75px"></a>
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent1" aria-controls="navbarSupportedContent1" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span></button>
	  <div class="collapse navbar-collapse" id="navbarSupportedContent1">
	    <ul class="navbar-nav mr-auto">
	      <li class="nav-item"> <a class="nav-link" href="index.html" >首页<span class="sr-only">(current)</span></a></li>
	      <li class="nav-item"> <a class="nav-link" href="report.html">报障</a></li>
	      <li class="nav-item"> <a class="nav-link" href="about.html" >关于计服</a></li>
            <li class="nav-item"><a class="nav-link" href="help.html" >帮助</a></li>
	      <li class="nav-item "> <a class="nav-link" href="login.html" style="color: #26A6FF">工作人员入口</a></li>
        </ul>
	    <form class="form-inline my-2 my-lg-0 col-lg-4 " action="http://localhost/GDPUjf/research.php" method="post">
				<input class="form-control mr-sm-2  col-lg-8" type="search" placeholder="输入电话号码查询生活区进度" aria-label="Search">
				<button class="btn btn-mybt my-2 my-sm-0" type="submit">查询</button>
			</form>
      </div>
</nav>
<!--内容-->
     <div class="container" style="padding-top:200px;">
     <div class="btn-group" style="margin: 0 auto;" >
         <a href="tea_unfinished.php?p=1"><button type="button" class="btn btn-default  btn btn-sm btn-mybt">教学区任务板块</button></a>
         <a href="unfinished.php?p=1"><button type="button" class="btn btn-default btn btn-sm   ">生活区任务板块</button></a>
     </div>
  </div>
    <div class="container" style="padding-top:50px;width:auto">
		<div class="title">
			<?php
		        $name=$_SESSION['name'];
		        echo "<h2 style='text-align: center'>欢迎你！".$name."</h2>" ;		           
		    ?>			
		</div>
	   <table class="imagetable" align="center">
          
		<p align="center"><br> 任务完成后请点击对应任务的完成按钮<br>点击<a href="tea_finished.php?p=1">已处理的任务</a>查看教学区已完成的任务。</p>
		<td colspan="11" align="center"><font size="3">教学区未处理任务</font></td>
		<tr>
			
			<th>姓名</th>
			<th>联系电话</th>
			<th>地址</th>
			<th>故障描述</th>
			<th>提交时间</th>
			<th>是否处理</th>
			<th>负责人</th>
			<th>完成时间</th>
			<th>操作</th>
			<?php		
		  //设置级别错误，通知类除外
		   error_reporting('E_ALL&~E_NOTICE');  
		   /**1---传入页码 ,使用GET获取**/
		  $page=$_GET['p'];
		   /**2---根据页码取出数据：php->mysql处理**/
		   $host=SAE_MYSQL_HOST_M;
		   $port=SAE_MYSQL_PORT;
		   $user =SAE_MYSQL_USER;
		   $pass =SAE_MYSQL_PASS;
		   $bdname =SAE_MYSQL_DB;
		   $pageSize=3;
		   $showPage=5;
		  	
		   //连接数据库,面向过程
		      $conn=mysqli_connect($host, $user, $pass, $bdname , $port); 
		      if(!$conn){
		          echo "数据库连接失败";
		          exit;
		      }
		      //选择所要操作的数据库
		      mysqli_select_db($conn,$bdname);
		      //设置数据库编码格式
		      mysqli_query($conn,"SET NAMES UTF8");
		      //编写sql获取分页数据 SELECT * FROM 表名 LIMIT 起始位置，显示条数
		     	$qid = mysqli_query($conn,"SELECT count(*) as total FROM teacher WHERE state='已处理'");//查询已处理条数
		     	$res = mysqli_fetch_array($qid);
		     	$done = $res['total'];
		     	$sql="SELECT * FROM teacher order by state ASC ,number ASC LIMIT ".(($page-1)*$pageSize+$done).",{$pageSize}";
		      $result=mysqli_query($conn,$sql);//把sql语句传送到数据库
		   /*-----表格部分-----*/
		   //echo "<div class='conntent'>";   //将数据显示到table中，并未table设置格式
		   //echo "<table border=1 cellspacing=0 width=30% align=center>";
		   while ($row = mysqli_fetch_assoc($result)) {
		        echo "<tr>";
		        echo "<td><font size='3px'>".$row['name']."</font></td>";
		        echo "<td><font size='3px'>".$row['tel']."</font></td>";
		        echo "<td><font size='3px'>".$row['adress']."</font></td>";
		        echo "<td><font size='3px'>".$row['description']."</font></td>";
		        echo "<td><font size='3px'>".$row['creat_time']."</font></td>";
		        echo "<td><font size='3px'>".$row['state']."</font></td>";
		        echo "<td><font size='3px'>".$row['responsible']."</font></td>";
		        echo "<td><font size='3px'>".$row['finish_time']."</font></td>";
		        echo "<td><a href='tea_operate.php?aim=".$row['tel']."' ><div class='btn btn-sm btn-mybt '>完成</div></a></td>";
		        echo "</tr>";
		   }
		   echo "</table>";
		   echo "</div>";
		  	 /*-----表格部分结束-----*/
		   //释放结果
		   mysqli_free_result($result);
		   //获取数据总条数
		  /*------分页部分-------*/
            $total_sql="SELECT COUNT(*)FROM teacher where state='未处理'";
		      $total_result=mysqli_fetch_array(mysqli_query($conn,$total_sql));
		      $total=$total_result[0];
		      $total_pages=ceil($total/$pageSize);
		   //关闭数据库
		   mysqli_close($conn);
		   /**3---显示数据+显示分页条**/
		   $page_banner="<nav aria-label='Page navigation example' class='pagination'> <ul class='pagination'>";
		   //计算偏移量
		   $pageoffset=($showPage-1)/2;
		   //两种情况下 首页、上一页 的显示效果
		   if($page>1){
		       $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=1'> 首页</a></li>";
		       $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=" .($page-1) . "'>&laquo;上一页</a></li>";
		   }else{
		       $page_banner .="<li class='page-item  disabled'><a class='page-link' href='#'>首页</a></li>   ";
		       $page_banner .="<li class='page-item disabled'><a class='page-link' href='#'> &laquo;上一页</a></li> ";
		   }
		   //显示
		   $start=1;
		   $end=$total_pages;
		   //当总条数大于分页数时
		   if($total_pages>$showPage){
		       if($page>$pageoffset+1){
		           $page_banner .="...";
		       }
		       if($page>$pageoffset){
		           $start=$page-$pageoffset;
		           $end=$total_pages>$page+$pageoffset?$page+$pageoffset:$total_pages;//三段式
		       }
		       //最前面几个特殊页号的显示。当前指的是页号1或者2时
		       else{
		           $start=1;
		           $end=$showPage;
		       }
		       //最后面几个特殊页号的显示，当前显示的是页号7和8
		       if($page+$pageoffset>$total_pages){
		           $start=$start-($page+$pageoffset-$end);//注意理解这一句
		       }
		   }
		   //显示页码
		   for($i=$start;$i<=$end;$i++){
		       //当前页页码上显示背景色
		       if($page==$i){
		           $page_banner .="<li class='page-item active'><span class='page-link'>{$i}<span class='sr-only'>(current)</span></span>";
		       }
		       //非当前页码显示
		       else{
		          // $page_banner .= "<a href='".$_SERVER['PHP_SELF']."?p=" .$i . "'>{$i}</a>"; 
		  			 $page_banner .=  "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=" .$i . "'>{$i}</a></li>";
		       }    
		   }
		   if($total_pages>$showPage&&$total_pages>$page+$pageoffset){
		       $page_banner .="...";    
		   }
		   //两种情况下的尾页、下一页 的显示效果
		   if($page<$total_pages){
		       $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=" .($page+1) . "'>下一页 &raquo;</a></li>";
		       $page_banner .= "<li class='page-item'><a class='page-link' href='".$_SERVER['PHP_SELF']."?p=$total_pages'>尾页</a></li>";
		   }else{
		       $page_banner .="<li class='page-item  disabled'><a class='page-link' href='#'>下一页&raquo;</a></li>  ";
		       $page_banner .="<li class='page-item disabled'><a class='page-link' href='#'>  尾页</a></li>";
		   }
		   $page_banner .= "共{$total_pages}页,";
		   $page_banner .= "<form action='tea_unfinished.php' method='get' class='form-inline my-2 my-lg-0'>";
		   $page_banner .= " 到第<input type='text' size=2 value='1' name='p' aria-describedby='basic-addon1' class='form-control'>页";
		   $page_banner .= "<input class='btn btn-sm btn-mybt 'type='submit' value='确定'>";
		   $page_banner .= "</form>";
		   $page_banner .= "</ul></nav>";
		   echo $page_banner;  
		?> 
		</tr>	
	</table>
	</div>

</body>
</html>