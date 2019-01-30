<!DOCTYPE html>
<html>
<body>

<h2>Registration</h2>

<form action="" method="post">
	{% csrf_token %}
<input type="text" name="firstname" placeholder="First Name">
<input type="text" name="lastname" placeholder="Last Name">
<input type="text" name="email" placeholder="Username">
<input type="password" name="password" placeholder="Password">

<input type="submit">
</form>

</body>
</html>
