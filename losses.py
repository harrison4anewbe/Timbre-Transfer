import tensorflow as tf
from tensorflow.keras.losses import BinaryCrossentropy

from config import LAMBDA

def l1_loss(target, output):
    return tf.reduce_mean(tf.abs(target - output))

def generator_loss(disc_generated_output, l1_value):
    loss_object = BinaryCrossentropy(from_logits=True)
    gan_loss = loss_object(tf.ones_like(disc_generated_output), disc_generated_output)
    total_gen_loss = gan_loss + (LAMBDA * l1_value)
    return total_gen_loss

def discriminator_loss(disc_real_output, disc_generated_output):
    loss_object = BinaryCrossentropy(from_logits=True)
    real_loss = loss_object(tf.ones_like(disc_real_output), disc_real_output)
    generated_loss = loss_object(tf.zeros_like(disc_generated_output), disc_generated_output)
    total_disc_loss = real_loss + generated_loss
    return total_disc_loss