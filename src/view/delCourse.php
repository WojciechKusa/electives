<?php
/**
 * Delete Course from database.
 */
?>
<div class="container">
    
    <?php
        $classTyp = $classType->fetchAll();
        $staf = $staff->fetchAll();
        $courses = $course->fetchAll();
        ?>
    <center>
<br><br><br><br>
<h1>Delete course</h1>
<br><br>
<form class="form-horizontal" method="POST" action="index.php?controller=store&action=delCourseFromDatabase" role="form"  style ="width:600px" id="register_form">
  <div class="form-group">
    <label class="col-sm-2 control-label">Choose course</label>
	<center>
    <div id="select" >
	<select name="idcourse">
		<?php
		for ( $i = 0; $i < count($courses); $i++ ){
			echo '<option value="'.$courses[$i]['idcourse'].'">'.' '.$courses[$i][0].' -  '.$courses[$i][1].'</option>';
		}
		?>
					 
	</select>
   </div>
	</center>
  </div>

  <button class="btn btn-lg btn-danger btn-block" type="submit" value="Dodaj">Delete</button>
</form>
<br><br><br><br>
    </center>

