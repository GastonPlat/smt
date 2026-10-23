with open('smt/surrogate_models/krg.py', 'r') as f:
    content = f.read()

# Let's check `krg.py` again to see what logic the user might be referring to.
# Maybe I should completely eliminate `_get_normalized_inputs` and `_get_normalized_outputs` if they are trivial?
# Wait! In `_update_predictive_parameters`, there is:
# Q, G = qr(Ft, mode="economic")
# ...
# IS there a method in `krg_based.py` for this?
