<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>Sign In</title>
<link rel="stylesheet" type="text/css" href="/artima.css" />
<link rel="shortcut icon" href="/favicon.ico" />
</head>
<body>
<div class="dialog"><table width="100%">
<tr valign="bottom">
<td align="left"><a href="/"><img src="/images/adl_dev.gif" alt="" style="border-width: 0" /></a></td>
</tr>
</table>
<hr style="width: 100%; margin: 0; padding: 0" /><br />

<p style="text-align: center">
<span style="font-size: 1.75em; color: darkslateblue; font-family: Verdana, Arial, Helvetica, sans-serif;">Please Sign In</span>
</p>

<form action="https://www.artima.com/sign_in" method="post" id="signInForm">
<div>
<input type="hidden" name="signIn" value="true" />
<input type="hidden" name="siteIDAsString" value="1" />
<input type="hidden" name="doneURL" value="spotlight/add.jsp?fromLogin=true" />
<table border="0" cellspacing="30" cellpadding="0" style="margin-left: auto; margin-right: auto">
<tr valign="top">
<td>
<br />
<div class="prettycontents">
<p>
<b>Don't have an Artima ID?</b><br />
Signing up is easy.<br />
</p>
<p style="text-align: right">
<b><a href="/account/new?d=spotlight%2Fadd.jsp%3FfromLogin%3Dtrue">Sign Up</a></b>
</p>
</div>
</td>

<td>
<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<div class="prettybox" style="background-color: #B0C4DE">

<table border="0" cellpadding="3" cellspacing="1">
<tr>
    <td>
        <span class="formlabel">
            Artima ID or<br />
            Email Address:
        </span>
    </td>
    <td>
    <input type="text" name="username"  value="" size="20" maxlength="60" />
    </td>
</tr>
<tr>
    <td>
        <span class="formlabel">Password:</span>
    </td>
    <td>
        <input type="password" name="password" size="20" maxlength="30" />
    </td>
</tr>
<tr>
    <td align="center" colspan="2" style="text-align: center; color: #333333">
    <label><input type="checkbox" name="rememberMe" /><span class="formlabel">Remember me</span></label></td>
</tr>
<tr>
<td colspan="2" align="center">
<input type="submit" name="signInButton" value="Sign In" />
</td>
</tr>
<tr>
<td colspan="2" align="center">
<span class="formcontents"><a href="http://www.artima.com/account/mailpwd?d=spotlight%2Fadd.jsp%3FfromLogin%3Dtrue">Forgot your password?</a></span>
</td>
</tr>

</table>
</div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</div>

</form>

<script type="text/javascript">
<!--
document.forms['signInForm'].username.focus();
//-->
</script>



<div class="smallprint">
<p style="text-align: center">
Copyright &copy; 2014 Artima, Inc. All rights reserved.
</p>
</div>
</div>
</body>
</html>