# The user wants me to use more utility methods.
# Is there an existing method in `utils.misc` or `mixed_int_corr.py`?
# "Check krg_based.py, distances.py, kernel_types.py, mixed_int_corr.py"

# Oh, in `kernel_types.py`, there is `is_scalar_encoding()`!
# In my `krg.py`:
#        kernel_handlers = {
#            MixIntKernelType.CONT_RELAX: self._apply_continuous_relaxation,
#            MixIntKernelType.DIST_ENCODING: self._apply_distributional_encoding,
#        }
# Is there a way to do something based on `is_scalar_encoding()`?
# For example, `MixIntKernelType.CONT_RELAX` requires continuous relaxation.
# `MixIntKernelType.DIST_ENCODING` requires DE distances.
# Gower, Compound Symmetry, etc. don't need anything more than what's returned by `gower_componentwise_distances` initially!
# So my code is fine!

# What if the user is referring to how I compute `X_new` vs `X_train` vs `X_new` distances?
# Look at `_predict_init` in `krg_based.py`:
