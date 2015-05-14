<?php

?>
<div class="container">
    
    <?php
        $classTyp = $classType->fetchAll();
        $staf = $staff->fetchAll();
        ?>
    <center>
<br><br><br><br>
<h1>Add course:</h1>
<br><br>
<form class="form-horizontal" method="POST" action="index.php?controller=store&action=addCourseToDatabase" role="form"  style ="width:600px" id="register_form">
   <div class="form-group">
    <label class="col-sm-2 control-label">Name: </label>
    <div class="col-sm-10">
      <input type="text" class="form-control" name="name" placeholder="Name" required autofocus>
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2 control-label">Coordinator</label>
	<center>
    <div id="select" >
	<select name="idstaff">
		<?php
		for ( $i = 0; $i < count($staf); $i++ ){
			echo '<option value="'.$staf[$i]['idstaff'].'">'.' '.$staf[$i]['name'].' '.$staf[$i]['surname'].' '.$staf[$i]['title'].' '.'</option>';
		}
		?>
					 
	</select>
   </div>
	</center>
	
  </div>
<div class="form-group">
    <label class="col-sm-2 control-label">ECTS: </label>
    <div class="col-sm-10">
      <input type="number" class="form-control" name="ects" min="1" max="30" required>
    </div>
  </div>
    <div class="form-group">
    <label class="col-sm-2 control-label">Course ID: </label>
    <div class="col-sm-10">
      <input type="number" class="form-control" name="id"  min="100" max="999999" placeholder="ID" required>
    </div>
  </div>
  <div class="form-group">
    <label class="col-sm-2 control-label">Number of hours: </label>
    <div class="col-sm-10">
      <input type="number" class="form-control" name="hours"  min="1" max="600" placeholder="Number of hours" required>
    </div>
  </div>
<div class="form-group">
    <label  class="col-sm-2 control-label">Description: </label>
    <div class="col-sm-10">
      <input type="text" class="form-control" style="height:200px" name="description" placeholder="Description" required>
    </div>
  </div>
    <div class="form-group">
    <label class="col-sm-2 control-label">Semester: </label>
    <div class="col-sm-10">
        <select class="form-control" name="semester" placeholder="Semester" required>
        <option value="0">Summer</option>
        <option value="1">Winter</option>
        </select>
    </div>
  </div>
      <div class="form-group">
    <label class="col-sm-2 control-label">Minimum students: </label>
    <div class="col-sm-10">
      <input type="number" class="form-control" name="minstudents"  min="1" max="200" placeholder="Min students" required>
    </div>
  </div>
      <div class="form-group">
    <label class="col-sm-2 control-label">Maximum students: </label>
    <div class="col-sm-10">
      <input type="number" class="form-control" name="maxstudents"  min="5" max="200" placeholder="Max students" required>
    </div>
  </div>
          <div class="form-group">
    <label class="col-sm-2 control-label">Class types: </label>
    <div class="col-sm-10 classtype">
        <?php
            for ( $i = 0; $i < count($classTyp); $i++ ){
                echo '<div>';
                echo '<input type="checkbox" class="toggle" data-idkursu="'.$i.'" name="classtype'.$classTyp[$i]['name'].'[]">'.' '.$classTyp[$i]['name'].'<br>';
                echo '<div class="select" >';
                echo '<select name="classidstaff[]">';
                for ( $j = 0; $j < count($staf); $j++ ){
                    echo '<option value="'.$staf[$j]['idstaff'].$classTyp[$i]['name'].'">'.' '.$staf[$j]['name'].' '.$staf[$j]['surname'].' '.$staf[$j]['title'].' '.'</option>';
		}
                echo '</select><br>';
                echo '<input type="number" data-idkursu="'.$i.'" class="form-control" name="classhours[]'.$classTyp[$i]['name'].'"  min="1" max="600" placeholder="Number of hours"><br><br>';
                echo '</div>';
                echo '</div>';
            }
	?>
    </div>
  </div>
    
  <button class="btn btn-lg btn-success btn-block" type="submit" value="Dodaj">Add</button>
</form>
<br><br><br><br>
    </center>

