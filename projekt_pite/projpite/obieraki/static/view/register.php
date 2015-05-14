<?php

?>
<div class="container">

<center>
<br><br><br>
<?php
	if($data == true && $error == "") {
		echo '<div class="alert alert-success" style="width:600px"><h2>Zarejestrowano pomyślnie!</h2></div>';
	}	
	else {
?>
	<div id="user_log">
	<?php if($error != '') echo '<div class="alert alert-danger" style="width:600px">'.$error.'</div>'; 
?>
<form class="form-signin" method="POST" action="index.php?controller=student&action=register" role="form" style="width:400px" id="register_form">
        <h2 class="form-signin-heading">Personal data: </h2>
        <input type="text" class="form-control" name="imie" placeholder="Name" required autofocus><br>
        <input type="text" class="form-control" name="nazwisko" placeholder="Surname" required><br>
        <input type="number" min="1" max="999999" class="form-control" name="indeks" placeholder="ID" required><br>
	<input type="email" class="form-control" name="mail" placeholder="Mail" required><br>
        <select class="form-control" name="kierunek" placeholder="Field of Study" required>
        <option value="Applied Computer Science">Computer Science</option>
        <option value="Theoretical Physics">Theoretical Physics</option>
        <option value="Philosophy">Philosophy</option>
        <option value="Cognitive Science">Cognitive Science</option>
        <option value="Mathematics">Mathematics</option>
        </select><br>
	<input type="number" min="1" max="5" class="form-control" name="rok" placeholder="Year" required><br>
	<input type="number" min="1" max="10" class="form-control" name="semestr" placeholder="Semester" required><br>

	<h2 class="form-signin-heading">Login data: </h2><br>
	<input type="text" class="form-control" name="login" placeholder="Login" required><br>
        <input type="password" class="form-control" name="haslo" placeholder="Hasło" required><br><br>

        <button class="btn btn-lg btn-success btn-block" type="submit" value="Rejestruj">Register</button>
</form>
<br><br>
<?php
	}
?>
</center>


