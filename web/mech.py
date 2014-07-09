#coding:utf-8
# http://wwwsearch.sourceforge.net/mechanize/   查看mechanize文档

from BeautifulSoup import BeautifulSoup, SoupStrainer
from mechanize import Browser

YOUR_LOGIN = ''
YOUR_PASSWD = ''

br = Browser()

rsp = br.open('http://us.pycon.org/2011/home')
print '\n***', rsp.geturl()
print 'Confirm home page has "Log in" link; click it'
page = rsp.read()
# Assert statements are a convenient way to insert debugging assertions into a program:
# assert_stmt ::=  "assert" expression ["," expression]
# , 'Log in not in page' 为当条件不为真时，自定义的所触发AssertError里面的错误信息
assert 'Log in' in page, 'Log in not in page'
# follow second link with element text matching regular expression
rsp = br.follow_link(text_regex='Log in')

# login page
print '***\n', rsp.geturl()
print 'Confirm at least a login form; submit invalid creds'
assert len(list(br.forms())) > 1, 'no forms on this page'
# br.select_form(name="order") 选择特定的form
br.select_form(nr=0)
br.form['username'] = YOUR_LOGIN
br.form['password'] = YOUR_PASSWD
rsp = br.submit()

# login page, with error
print '\n***',rsp.geturl()
print 'Error due to invalid creds; resubmit w/valid creds'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/login', rsp.geturl()

page = rsp.read()
err = str(BS(page).find("div",
		{"id":"errorMsg"}).find('ul').find('li').string)
assert err == 'The username and/or password you specified are not correct.', err
br.select_form(nr=0)
br.form['username'] = YOUR_LOGIN
br.form['password'] = YOUR_PASSWD
rsp = br.submit()

# login successful, home page redirect
print '\n***', rsp.geturl()
print 'Logged in properly on home page; click Account link'
assert rsp.geturl() == 'http://us.pycon.org/2011/home/', rsp.geturl()
page = rsp.read()
assert 'Logout' in page, 'Logout not in page'
rsp = br.follow_link(text_regex='Account')

# account page
print '\n***', rsp.geturl()
print 'Email address parseable on Account page; go back'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/email', rsp.geturl()
page = rsp.read()
assert 'Email Addresses' in page, 'Missing email addresses'
print '	Primary e-mail: %r' % str(
	BS(page).find('table').find('tr').find('td').find('b').string)
rsp = br.back()

# back to home page
print '\n***', rsp.geturl()
print 'Back works, on home page again; click Logout link'
assert rsp.geturl() == 'http://us.pycon.org/2011/home/', rsp.geturl()
rsp = br.follow_link(url_regex='logout')

# logout page
print '\n***', rsp.geturl()
print 'Confirm on Logout page and Log in link at the top'
assert rsp.geturl() == 'http://us.pycon.org/2011/account/logout', rsp.geturl()
page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
print '\n*** Done'



