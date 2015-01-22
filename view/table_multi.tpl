<!--Table Widget Start-->
<div class = 'table-responsive'>
  <table class = "table table-striped table-hover table-bordered ">
    <thead>
      <tr>
        %for field in widget.fields:
        <th>{{field}}</th>
        %end
      </tr>
    </thead>
    <tbody>
      %for row in widget.data:
      <tr>
        %for value in row:
        <td>{{value}}</td>
        %end
      </tr>
      %end
    </tbody>
  </table>
</div> 
<!--Table Widget End-->
