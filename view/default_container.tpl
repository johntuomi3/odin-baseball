%include('view/header.tpl')
	%include('view/nav.tpl')
    <!--Your site content starts-->
    <div class="container col-xs-12">
        %include({{widget}})
    </div>
    <!-- Your site ends -->
%include('view/footer.tpl')