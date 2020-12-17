# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

# Example

#     For sequence = [1, 3, 2, 1], the output should be
#     almostIncreasingSequence(sequence) = false.

#     There is no one element in this array that can be removed in order to get a strictly increasing sequence.

#     For sequence = [1, 3, 2], the output should be
#     almostIncreasingSequence(sequence) = true.

#     You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
def almostIncreasingSequence(seq):
  # Keep track of the previous item in the list, for comparison.
  # Note that we set it to the first item in the sequence, since
  # it doesn't have a previous item.
  prev = seq[0]

  # Number of values that would have to be removed in order for the sequence
  # to be strictly increasing.
  counter = 0

  # Iterate over the sequence, but skip the first one (we don't have a previous
  # value to compare against).
  for i in range(1, len(seq)):
    if seq[i] <= prev:
      counter += 1

      # If we've determined that more than one item would need to be removed,
      # then we don't need to continue.
      if counter > 1:
        return False

      #
      # Peek back 2 positions to determine whether we should remove ``prev`` or
      # ``seq[i]``.
      #
      # Examples:
      #
      # [2, 10, 1, ...]
      #  ^  ^^  ^
      #  |  ||  |
      #  |  ||  seq[i]
      #  |  prev
      #  seq[i-2]
      #
      # If we remove ``prev``, we still don't have a strictly-increasing
      # sequence, because ``seq[i]`` is still less than ``seq[i-2]``.
      #
      # Therefore, we should remove ``seq[i]`` from the sequence.
      #
      # ---
      #
      # [1, 10, 2, 3, ...]
      #  ^  ^^  ^
      #  |  ||  |
      #  |  ||  seq[i]
      #  |  prev
      #  seq[i-2]
      #
      # In this scenario, we can maintain a strictly increasing sequence by
      # removing either ``prev`` or ``seq[i]``.
      #
      # However, we will have a better chance of ending up with a strictly-
      # increasing sequence if we remove the larger value (``prev``).
      #
      # ---
      #
      # [10, 1, 2, ...]
      #  ^^  ^
      #  ||  |
      #  ||  seq[i]
      #  prev
      #
      # In this scenario, we are too close to the start of the sequence to peek
      # back 2 positions.  As with the previous scenario, we should remove the
      # larger value so that we have the best chance of ending up with a
      # strictly-increasing sequence.
      #
      if (i < 2) or (seq[i-2] < seq[i]):
        prev = seq[i]
    else:
      # So far we have an increasing sequence.  Advance 1 position.
      prev = seq[i]

  # We reached the end of the sequence, and ``counter`` never exceeded 1.
  return True


# Happy path
assert almostIncreasingSequence([1, 2, 3, 4, 5, 10]) is True
assert almostIncreasingSequence([1, 2, 4, 3, 5, 10]) is True

# Repeated values
assert almostIncreasingSequence([1, 2, 3, 3, 4, 5]) is True
assert almostIncreasingSequence([1, 2, 3, 3, 3, 4, 5]) is False

# First item is largest
assert almostIncreasingSequence([10, 1, 2, 3, 4, 5]) is True
assert almostIncreasingSequence([10, 1, 2, 3, 5, 4]) is False

# Last item is largest
assert almostIncreasingSequence([1, 2, 3, 5, 5, 5]) is False
assert almostIncreasingSequence([1, 2, 4, 3, 5, 5]) is False

# Largest item disrupts sequence
assert almostIncreasingSequence([10, 20, 30, 100, 40, 50]) is True
assert almostIncreasingSequence([10, 50, 60, 100, 20, 30]) is False
assert almostIncreasingSequence([10, 60, 50, 100, 20, 30]) is False

# Two sub-sequences
assert almostIncreasingSequence([40, 50, 60, 10, 20, 30]) is False

# Short sequences
assert almostIncreasingSequence([1]) is True
assert almostIncreasingSequence([1, 1]) is True