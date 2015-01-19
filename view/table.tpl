<!--Table Widget Start-->
<div class = 'table-responsive'>
	<table class = "table table-striped table-hover table-bordered ">
		<thead>
			<tr>
				%for field in fields:
				<th>{{field}}</th>
				%end
			</tr>
		</thead>
		<tbody>
				%for row in data: 
		  <tr>  
			%for value in row:
					<td>{{value}}</td>
			%end
		  </tr>
				%end
		</tbody>
	</table>
<!--Table Widget End-->
