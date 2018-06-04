{% import 'inputhelper.tpl' as helper %}

<p>{{ helper.input('username') }}</p>
<p>{{ helper.input('password', type='password') }}</p>