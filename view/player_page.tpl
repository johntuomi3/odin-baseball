%include('view/header.tpl')
    %include('view/nav.tpl')
    <div class="container-fluid">
        <!--Your site content starts-->
                %for widget in widgets:
				<div class="row">
					<div class="container col-xs-9">
		            %if widget.name == 'panel':	
			            %include('view/panel_multi.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
					%elif widget.name == 'card':
			            %include('view/card_multi.tpl')
		            %end
					</div>
				</div>
                %end
    </div>
 <!-- Your site ends -->
%include('view/footer.tpl')