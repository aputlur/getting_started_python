def method_args(mandatory_parameter, default_parameter="Default_value", *tuples, **dictionaries):

    print("mandatory_parameter = {}{}, default_parameter = {}{}, tuples_var = {}{}, dict_var = {}{}" .format(mandatory_parameter,type(mandatory_parameter),default_parameter,type(default_parameter),tuples,type(tuples), dictionaries,type(dictionaries)))

method_args("anil")
method_args("kumar", "reddy")
method_args("anil","kumar", "('roopa','kallam)", '1:Bhairav, 2:tarini, 3: Abc')
