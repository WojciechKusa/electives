<?php

?>
<div class="container">

<center>
<br><br><br><br>
<?php
	if($data == true && $error == "") {
            echo $userData['idUser_2'];
		echo '<div class="alert alert-success" style="width:600px"><h2>Login succeded!</h2></div>';
	}	
	else {
?>
	<div id="user_log">
	<?php if($error != '') echo '<div class="alert alert-danger" style="width:600px">'.$error.'</div>'; 
?>
<form class="form-signin" method="POST" action="index.php?controller=student&action=logIn" role="form" style="width:300px" id="login_form">
        <h2 class="form-signin-heading">Log in</h2>
        <input type="text" class="form-control" name="login" placeholder="Login" required autofocus><br>
        <input type="password" class="form-control" name="haslo" placeholder="Password" required><br>
        <button class="btn btn-lg btn-success btn-block" type="submit" value="Loguj">Log in</button><br>
	<button type="button" class="btn btn-lg btn-primary btn-block" onclick="location='index.php?controller=student&action=register'">Sign up</button>
</form>
<?php
	}
?>
</center>


