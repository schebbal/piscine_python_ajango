function displayFormContents() {

	var out = '';

	out += 'Firstname = ' + document.getElementById('firstname').value + '\n';
	out += 'Name = '      + document.getElementById('name').value      + '\n';
	out += 'Phone = '     + document.getElementById('phone').value     + '\n';
	out += 'Age = '       + document.getElementById('age').value       + '\n';
	out += 'Email = '     + document.getElementById('email').value     + '\n';

	out += 'Gender = ';
	if (document.getElementById('male').checked == true)
		out += document.getElementById('male').value;
	if (document.getElementById('female').checked == true)
		out += document.getElementById('female').value;
	if (document.getElementById('other').checked == true)
		out += document.getElementById('other').value;
	out += '\n';

	if (document.getElementById('student42').checked == true)
		out += 'Student at 42 = yes';
	else
		out += 'Student at 42 = no';

	alert(out);

}