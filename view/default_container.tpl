%include('view/header.tpl')
	%include('view/nav.tpl')
    <!--Your site content starts-->
    <div class="container col-xs-12">
		%if widget == 'panel':	
			%include('view/panel.tpl')
		%elif widget == 'table':
			%include('view/table.tpl')
		%elif widget == 'card':
			%include('view/card.tpl')
		%end
    </div>
	<noscript>
		{{widget}}
	</noscript>
    <!-- Your site ends -->
%include('view/footer.tpl')