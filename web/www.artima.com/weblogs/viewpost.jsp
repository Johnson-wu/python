




<html>
<head>
<title>Security Debt</title>
<meta name="author" content="Johan Peeters" />
<link rel="stylesheet" type="text/css" href="/artima.css" />
<link rel="shortcut icon" href="/favicon.ico" />
</head>
<body><table width="100%" cellspacing="0">
<tr>
<td align="left" valign="bottom">
<a href="/index.jsp"><img src="/images/a7.gif" alt="The Artima Developer Community" border="0" width="550" height="43" /></a>
</td>
</table>
<table width="100%" bgcolor="#333333">
<tr>
<td align="center">
<div class="ml">
<a href="/articles" class="hl">Articles</a>&nbsp;|
<a href="/news/index.jsp" class="hl">News</a>&nbsp;|
<a href="/weblogs/index.jsp" class="hl">Weblogs</a>&nbsp;|
<a href="/buzz/index.jsp" class="hl">Buzz</a>&nbsp;|
<a href="/shop/catalog" class="hl">Books</a>&nbsp;|
<a href="/forums/index.jsp" class="hl">Forums</a>
</div>
</td>
</tr>
</table>
<table width="100%" bgcolor="#CCCCCC">
<tr>
<td align="center">
<div class="sc">
<a href="/weblogs/index.jsp">Artima Weblogs</a>&nbsp;| 

<a href="/weblogs/index.jsp?blogger=yo">Johan Peeters' Weblog</a>&nbsp;| 

<a href="/forums/flat.jsp?forum=106&thread=320875">Discuss</a>&nbsp;| 
<a href="mailto:?subject=Security Debt&body= %0AArtima Weblogs %0ASecurity Debt %0Aby Johan Peeters %0A%0Ahttp://www.artima.com/weblogs/viewpost.jsp?thread=320875">Email</a>&nbsp;| 
<a href="viewpostP.jsp?thread=320875">Print</a>&nbsp;| 
<a href="/weblogs/bloggers.jsp">Bloggers</a>&nbsp;| 
<a class= "sl" href="viewpost.jsp?thread=200967" title="Dreams and Nightmares">Previous</a></a>&nbsp;| 
Next</a>
</div>
</td>
</tr>
</table>
<table width="100%" bgcolor="#EEEEEE">
<tr>
<td align="center">
<div class="sc">
<span style="color: #555555">Sponsored Link</span> <span style="color: #888888">&bull;</span> 
<script language='JavaScript' type='text/javascript' src='http://www.artima.com/zcr/adx.js'></script>
<script language='JavaScript' type='text/javascript'>
<!--
   if (!document.phpAds_used) document.phpAds_used = ',';
   phpAds_random = new String (Math.random()); phpAds_random = phpAds_random.substring(2,11);
   
   document.write ("<" + "script language='JavaScript' type='text/javascript' src='");
   document.write ("http://www.artima.com/zcr/adjs.php?n=" + phpAds_random);
   document.write ("&amp;what=zone:9&amp;target=_top");   document.write ("&amp;exclude=" + document.phpAds_used);
   if (document.referrer)
      document.write ("&amp;referer=" + escape(document.referrer));
   document.write ("'><" + "/script>");
//-->
</script><noscript><a href='http://www.artima.com/zcr/adclick.php?n=a799ecf6' target='_top'><img src='http://www.artima.com/zcr/adview.php?what=zone:9&amp;n=a0587811' border='0' alt=''></a></noscript>
</div>
</td>
</tr>
</table>
<BR>
<div class="vegies">
<div class="tc">
<span class="sts">Thinking Aloud</span><br />
<span class="ts">Security Debt</span><br />
<span class="as">by Johan Peeters</span><br />
<span class="pd">March 6, 2011</span><br />
</div>




<blockquote>
<b>Summary</b><br>
Chris Wysopal likens application security debt to technical debt in a couple of recent blog posts. It turns out that the debt metaphor is particularly apt as, like financial debt, application security debt is susceptible to interest rate fluctuations.

</blockquote>

<hr align="left" width="90%">



<table align="right">
<tr>
<td>
<div class="adnotice">
Advertisement
</div>
<center>
<script language='JavaScript' type='text/javascript' src='http://www.artima.com/zcr/adx.js'></script>
<script language='JavaScript' type='text/javascript'>
<!--
if (!document.phpAds_used) document.phpAds_used = ',';
phpAds_random = new String (Math.random()); phpAds_random = phpAds_random.substring(2,11);
document.write ("<" + "script language='JavaScript' type='text/javascript' src='");
document.write ("http://www.artima.com/zcr/adjs.php?n=" + phpAds_random);
document.write ("&amp;what=zone:2");
document.write ("&amp;exclude=" + document.phpAds_used);
if (document.referrer)
document.write ("&amp;referer=" + escape(document.referrer));
document.write ("'><" + "/script>");
//-->
</script><noscript><a href='http://www.artima.com/zcr/adclick.php?n=a74ab060' target='_blank'><img src='http://www.artima.com/zcr/adview.php?what=zone:2&amp;n=a74ab060' border='0' alt=''></a></noscript>

</center>
 </td>
</tr>
</table>

<p>
<p>
Chris Wysopal likens <a href="http://www.veracode.com/blog/2011/02/application-security-debt-and-application-interest-rates/">application security debt</a> to <a href="http://c2.com/doc/oopsla92.html">technical debt</a> in <a href="http://www.veracode.com/blog/2011/03/a-financial-model-for-application-security-debt/">a couple of recent blog posts</a>. It turns out that the debt metaphor is particularly apt as, like financial debt, application security debt is susceptible to interest rate fluctuations.
</p>
<p>
The threat landscape changes in the application's life time. Unfortunately, security interest rates are much more likely to go up than down as new vulnerabilities are disclosed and the application gains mind share. The former makes it easier for attackers to compromise the application, the latter provides them with a greater incentive. An effect that Chris missed is the tendency for an application to increase its attack surface as it is extended with new functionality.
</p>
<p>
Leverage through financial debt can help a company grow and, similarly, so can technical debt. However, as interest rates become punitive, clearly the time to de-leverage has come. Chris presents a model to quantify the dollar cost of the debt, but, frankly, the calculations are tenuous, as he admits himself. I would feel happier with qualitative guidelines. What do you think the tell-tale signs are for the need to de-leverage?
</p>

<h1>Talk Back!</h1>

<p>
Have an opinion?


Readers have already posted

<a href="../forums/flat.jsp?forum=106&thread=320875">5

comments</a>
about this weblog entry. Why not

<a href="../forums/post.jsp?forum=106&thread=320875&reply=true">add yours</a>?


<h1>RSS Feed</h1>

<p>
If you'd like to be notified whenever Johan Peeters adds a new entry to <a href="index.jsp?blogger=yo">his weblog</a>, subscribe to his <a href="feeds/bloggers/yo.rss">RSS feed</a>.

<center>
<div class="sociallinks">
  <a href="http://digg.com/submit?phase=2&url=http%3A%2F%2Fwww.artima.com%2Fweblogs%2Fviewpost.jsp%3Fthread%3D320875&title=Security+Debt&bodytext=Chris+Wysopal+likens+application+security+debt+to+technical+debt+in+a+couple+of+recent+blog+posts.+It+turns+out+that+the+debt+metaphor+is+particularly+apt+as%2C+like+financial+debt%2C+application+security+debt+is+susceptible+to+interest+rate+fluctuations.&topic=programming">
    <img src="/images/digg.gif" alt="Digg"
         border="0" height="14" hspace="8" width="16" />Digg
  </a>
  |
  <a href="http://del.icio.us/post?url=http%3A%2F%2Fwww.artima.com%2Fweblogs%2Fviewpost.jsp%3Fthread%3D320875&title=Security+Debt">
    <img src="/images/delicious.gif" alt="del.icio.us" 
         border="0" height="16" hspace="8" width="16" vspace="1" />del.icio.us
  </a>
  |
  <a href="http://programming.reddit.com/submit?url=http%3A%2F%2Fwww.artima.com%2Fweblogs%2Fviewpost.jsp%3Fthread%3D320875&title=Security+Debt">
    <img src="/images/reddit.gif" alt="Reddit" 
         border="0" height="18" hspace="8" width="18" />Reddit
  </a>  
</div>
</center>

<h1>About the Blogger</h1>

<P>
<table><tr valign="bottom"><td><img src="../images/johanpeeters.jpg" align="right"></td><td>Johan Peeters is an independent software architect who spends a lot of 
time plumbing and generally fixing leaks.</td></tr></table><p>

<div class="sp">This weblog entry is Copyright &copy; 2011 Johan Peeters. All rights reserved.</div>
</div>

</div>
<hr width="100%" />
<table width="50%" align="center">
<tr>
<td>
<div class="horizontaltextadbox">
<div class="adheadline">Sponsored Links</div>
<div id="sponsoredlinks">
</div>
</div>
</td>
</tr>
</table>
<hr width="100%" />
<center>
<script type="text/javascript"><!--
google_ad_client = "pub-3911176865765226";
google_alternate_color = "ffffff";
google_ad_width = 728;
google_ad_height = 15;
google_ad_format = "728x15_0ads_al";
google_ad_channel = "";
google_color_border = "ffffff";
google_color_bg = "FFFFFF";
google_color_link = "003090";
google_color_text = "000000";
google_color_url = "666666";
//--></script>
<script type="text/javascript"
  src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
<br />
<br />
<!-- SiteSearch Google -->
<form method="get" action="http://www.google.com/custom">
<table border="0" bgcolor="#ffffff">
<tr><td nowrap="nowrap" valign="top" align="left" height="32">
<a href="http://www.google.com/">
<img src="http://www.google.com/logos/Logo_25wht.gif"
border="0" alt="Google"></img></a>
</td>
<td nowrap="nowrap">
<input type="hidden" name="domains" value="Artima.com"></input>
<input type="text" name="q" size="31" maxlength="255" value=""></input>
<input type="submit" name="sa" value="Search"></input>
</td></tr>
<tr>
<td>&nbsp;</td>
<td nowrap="nowrap">
<font size="-1" color="#000000">
<input type="radio" name="sitesearch" value=""></input> Web
<input type="radio" name="sitesearch" value="Artima.com" checked="checked"></input>Artima.com
</font>&nbsp;&nbsp;
<input type="hidden" name="client" value="pub-3911176865765226"></input>
<input type="hidden" name="forid" value="1"></input>
<input type="hidden" name="ie" value="ISO-8859-1"></input>
<input type="hidden" name="oe" value="ISO-8859-1"></input>
<input type="hidden" name="cof" value="GALT:#008000;GL:1;DIV:#336699;VLC:663399;AH:center;BGC:FFFFFF;LBGC:FFFFFF;ALC:0000FF;LC:0000FF;T:000000;GFNT:0000FF;GIMP:0000FF;LH:50;LW:150;L:http://www.artima.com/images/artima150.gif;S:http://www.artima.com;FORID:1;"></input>
<input type="hidden" name="hl" value="en"></input>
</td></tr></table>
</form>
<!-- SiteSearch Google -->
</center>
<br />
<div class="sp">
<div style="text-align: center">
<a href="http://www.artima.com/copyright.html">Copyright</a> &copy; 1996-2014 Artima, Inc. All Rights Reserved.</a> - <a href="http://www.artima.com/privacy.html">Privacy Policy</a> - <a href="http://www.artima.com/termsofuse.html">Terms of Use</a> - <a href="http://www.artima.com/advertising.html">Advertise with Us</a>
</div>
</div>
<br />
<script language='JavaScript' type='text/javascript'>
<!--
function initBannerVarForZone(zone) {
        initBannerVarForZoneWithScript(zone, 'adjs_modified');
}

function initBannerVarForZoneWithScript(zone, phpScript) {

        if (!document.phpAds_used) document.phpAds_used = ',';
        phpAds_random = new String (Math.random());
        phpAds_random = phpAds_random.substring(2,11);

        var nextScriptSrc = 'http://www.artima.com/zcr/' + phpScript + '.php?n=' +
                phpAds_random  +
                '&amp;what=zone:' + zone + '&amp;target=_top&amp;block=1&amp;blockcampaign=1' +
                '&amp;exclude=' + document.phpAds_used;

        document.write("<script language='JavaScript' type='text/javascript' src='");
        document.write(nextScriptSrc);
        document.write("'><\/script>");

}

function replaceDiv(divID) {
        document.getElementById(divID).innerHTML = phpadsbanner;
}
-->
</script>
<script language='JavaScript' type='text/javascript'>
<!--
initBannerVarForZone(3);
-->
</script>

<script language='JavaScript' type="text/javascript">
<!--
replaceDiv('leftskyscraper');
-->
</script>
<script language='JavaScript' type='text/javascript'>
<!--
initBannerVarForZoneWithScript(4, 'textman');
-->
</script>

<script language='JavaScript' type="text/javascript">
<!--
replaceDiv('sponsoredlinks');
-->
</script>
</body>
</html>
