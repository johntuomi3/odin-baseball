%include('view/header.tpl')
    %include('view/nav.tpl')
    <div class="container-fluid">
        <!--Your site content starts-->
        <div class="row">
            <div class="container col-xs-3">
                %for widget in widgets_topleft:
		            %if widget.name == 'panel':	
			            %include('view/panel.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
		            %end
                %end
            <noscript>
		        {{widgets_topleft}}
	        </noscript>
            </div>
            <div class="container col-xs-6">
                %for widget in widgets_topmiddle:
		            %if widget.name == 'panel':	
			            %include('view/panel.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
		            %end
                %end
            <noscript>
		        {{widgets_topmiddle}}
	        </noscript>
            </div>
            <div class="container col-xs-3">
                %for widget in widgets_topright:
		            %if widget.name == 'panel':	
			            %include('view/panel.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
		            %end
                %end
            <noscript>
		        {{widgets_topright}}
	        </noscript>
            </div>
        </div>
        <div class="row">
            <div class="container col-xs-3">
                %for widget in widgets_bottomleft:
		            %if widget.name == 'panel':	
			            %include('view/panel.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
		            %end
                %end
            <noscript>
		        {{widgets_bottomleft}}
	        </noscript>
            </div>
            <div class="container col-xs-6">
                %for widget in widgets_bottommiddle:
		            %if widget.name == 'panel':	
			            %include('view/panel.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
		            %end
                %end
            <noscript>
		        {{widgets_bottommiddle}}
	        </noscript>
            </div>
            <div class="container col-xs-3">
                %for widget in widgets_bottomright:
		            %if widget.name == 'panel':	
			            %include('view/panel.tpl')
		            %elif widget.name == 'table':
			            %include('view/table_multi.tpl')
		            %end
                %end
            <noscript>
		        {{widgets_bottomright}}
	        </noscript>
            </div>
        </div>
    </div>
 <!-- Your site ends -->
%include('view/footer.tpl')