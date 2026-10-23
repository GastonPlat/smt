# Ah! In `_apply_continuous_relaxation`:
#        X1_unfolded, _, unfolded_cat = self.design_space.unfold_x(X1)
#        X2_unfolded, _, _ = self.design_space.unfold_x(X2)
#        X1_norma = (X1_unfolded - self.X2_offset) / self.X2_scale
#        X2_norma = (X2_unfolded - self.X2_offset) / self.X2_scale
#        D = np.abs(differences(X1_norma, Y=X2_norma.copy()))
#
# Wait, this logic is EXACTLY what `_predict_init` and `_compute_training_distances` do!
# If the user says "there are probably already methods for some of the operations the helper functions are processing", could it be `_correct_distances_cat_decreed`?
# I DO USE `_correct_distances_cat_decreed`.
