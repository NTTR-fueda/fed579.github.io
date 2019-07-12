#!/usr/local/bin/perl

#��������������������������������������������������������������������
#�� FullPath Viewer : fullpath.cgi - 2011/09/21
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
#��������������������������������������������������������������������
#�� [���ӎ���]
#�� 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����
#��    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B
#�� 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B
#��    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B
#��������������������������������������������������������������������

# ���W���[���錾
use strict;
use CGI::Carp qw(fatalsToBrowser);

# �o�[�W�������
my $ver = 'FullPath Checker v1.6';

# ������
my %path;

# ��P�`�F�b�N
eval{ $path{1} = `pwd`; };
if ($@ || $path{1} eq "") { $path{1} = 'unknown'; }

# ��Q�`�F�b�N
$path{2} = $0 =~ /^(.*[\\\/])/ ? $1 : 'unknown';

# ��R�`�F�b�N
$path{3} = $ENV{SCRIPT_FILENAME} || 'unknown';

print <<EOM;
Content-type: text/html

<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=shift_jis">
<meta http-equiv="content-style-type" content="text/css">
<style type="text/css">
<!--
body { font-size:80��; }
dd { color: #dd0000; font-family:Verdana,Helvetica,Arial; }
p { font-family:Verdana,Helvetica,Arial;font-size:10px;text-align:center; }
-->
</style>
<title>$ver</title>
</head>
<body>
<h3>���́u�f�B���N�g���v�̃t���p�X�`�F�b�N�̌��ʂ͈ȉ��̂Ƃ���ł��B</h3>
- �uunknown�v�Əo��ꍇ�ɂ͎擾�Ɏ��s�����ꍇ�ł� -
<dl>
	<dt>��1�`�F�b�N</dt>
	<dd>$path{1}</dd>
	<dt>��2�`�F�b�N</dt>
	<dd>$path{2}</dd>
	<dt>��3�`�F�b�N</dt>
	<dd>$path{3}</dd>
</dl>
<!-- ���쌠�\\���i�폜�s�j-->
<p>- <a href="http://www.kent-web.com/">Fullpth Viewer</a> -</p>
</body>
</html>
EOM

