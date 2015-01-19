<!--Your site content starts-->
<table class = "table table-striped table-hover ">
	<thead>
		<tr>
			%for field in fields:
			<th>{{field}}</th>
			%end
		</tr>
	</thead>
	<tbody>
		<tr>
			%for value in values:
			<td>{{value}}</td>
			%end
		</tr>
	</tbody>
</table>
<!-- Your site ends here -->
