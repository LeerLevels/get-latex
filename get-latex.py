def getLatex(input, custom_options={}):

  def getNonScientific(input, options):
    num_decimals = options["num_decimals"]
    rounded = round(input,num_decimals)
    value_string = str(rounded)
    if "." in value_string:
      value_string = value_string.replace(".",options["output_delimiter"])
    non_scientific = options["wrapper"]+value_string+options["wrapper"]
    return non_scientific

  def getScientific(input, options):
    input_pre_post_power = getPrePostPower(input, options)
    pre = input_pre_post_power["pre"]
    post = input_pre_post_power["post"]
    power = input_pre_post_power["power"]
    scientific = options["wrapper"]+str(pre)
    if post:
      scientific += options["output_delimiter"] + str(post)
    if power != 0:
      scientific += " \\cdot 10^{"+str(power)+"}"
    scientific += options["wrapper"]
    return scientific

  def getPrePostPower(input, options):
    pre_comma_digits = options["pre_comma_digits"]
    num_significant = options["num_significant"]
    ten_power = math.log(input,10)
    ten_power_floored = math.floor(ten_power)
    ten_power_floored_inverted = -1*ten_power_floored
    ten_shift = ten_power_floored_inverted + pre_comma_digits - 1
    shifted_float = round(input*10**ten_shift,5) # Rounding should not be hard-coded
    pre = shifted_float // 1
    num_decimals = num_significant-pre_comma_digits
    if num_decimals <= 0:
      num_decimals = 0
    post_unrounded = shifted_float-pre
    if num_decimals == 0 and post_unrounded > 0.5:
      pre += 1
    post = int(round(post_unrounded,num_decimals)*10**num_decimals)
    if num_significant <= pre_comma_digits:
      post = False
    output = {"pre": int(pre), "post": post, "power": int(ten_power_floored),"shifted_float": shifted_float,"post_unrounded": post_unrounded, "num_decimals": num_decimals}
    # print(output)
    return output
  
  # Set default options
  options = {
    "use_scientific": True,
    "pre_comma_digits": 1,
    "num_significant": 3,
    "num_decimals": 2, # only for non-scientific formatting
    "wrapper": "$",
    "output_delimiter": "{,}"
  }
  # Update defaults with optional custom options
  if custom_options:
    for key in custom_options:
      options[key] = custom_options[key]
  # Return correct function
  if options["use_scientific"]:
    return getScientific(input, options)
  else:
    return getNonScientific(input, options)
