a = '''
Abstract—1 In recent years, deep learning has
revolutionized the field of machine learning, for
computer vision in particular. In this approach, a deep
(multilayer) artificial neural network (ANN) is trained
in a supervised manner using backpropagation. Vast
amounts of labeled training examples are required, but
the resulting classification accuracy is truly impressive,
sometimes outperforming humans. Neurons in an ANN
are characterized by a single, static, continuous-valued
activation. Yet biological neurons use discrete spikes to
compute and transmit information, and the spike times,
in addition to the spike rates, matter. Spiking neural
networks (SNNs) are thus more biologically realistic than
ANNs, and arguably the only viable option if one wants
to understand how the brain computes. SNNs are also
more hardware friendly and energy-efficient than ANNs,
and are thus appealing for technology, especially for
portable devices. However, training deep SNNs remains a
challenge. Spiking neurons’ transfer function is usually
non-differentiable, which prevents using backpropagation.
Here we review recent supervised and unsupervised
methods to train deep SNNs, and compare them in
terms of accuracy, but also computational cost and
hardware friendliness. The emerging picture is that
SNNs still lag behind ANNs in terms of accuracy,
but the gap is decreasing, and can even vanish on some
tasks, while SNNs typically require many fewer operations.
'''.replace('\n', " ")
# print(a)
