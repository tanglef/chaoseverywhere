The logistic map
=========================

Definitions
--------------------
The logistic map is a recursive sequence defined as:

.. math::

   x_{n+1}=rx_n(1-x_n),


where :math:`r\in [1,4]` is the growth ratio and with :math:`x_0\in[0,1]`.
The goal of this module is to be able tu visualize the logistic map, but also to create its bifurcation diagram and link it to the Mandelbrot set.

The bifurcation diagram is a plot of where the logistic map tends to. It shows us that as the growth ratio approaches :math:`4`,
the chaotic behaviour appears.


Summary of the outputs
-----------------------------

.. raw:: html

   <style type="text/css">
   .tg  {border-collapse:collapse;border-spacing:0;border-color:#aabcfe;}
   .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 18px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#669;background-color:#e8edff;}
   .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 18px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#039;background-color:#b9c9fe;}
   .tg .tg-phtq{background-color:#D2E4FC;border-color:inherit;text-align:left;vertical-align:top}
   .tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
   .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
   .tg .tg-svo0{background-color:#D2E4FC;border-color:inherit;text-align:center;vertical-align:top}
   </style>
   <p>
   <table class="tg">
     <tr>
       <th class="tg-0pky">Methods</th>
       <th class="tg-c3ow" colspan="3">Output</th>
     </tr>
     <tr>
       <td class="tg-phtq"></td>
       <td class="tg-svo0">float</td>
       <td class="tg-svo0">video</td>
       <td class="tg-svo0">matplotlib plot</td>
     </tr>
     <tr>
       <td class="tg-0pky">animate_logistic</td>
       <td class="tg-c3ow"></td>
       <td class="tg-c3ow">X</td>
       <td class="tg-c3ow"></td>
     </tr>
     <tr>
       <td class="tg-phtq">connections</td>
       <td class="tg-svo0"></td>
       <td class="tg-svo0">X</td>
       <td class="tg-svo0"></td>
     </tr>
     <tr>
       <td class="tg-0pky">logistic</td>
       <td class="tg-c3ow">X</td>
       <td class="tg-c3ow"></td>
       <td class="tg-c3ow"></td>
     </tr>
     <tr>
       <td class="tg-phtq">logistic_draw</td>
       <td class="tg-svo0"></td>
       <td class="tg-svo0"></td>
       <td class="tg-svo0">X</td>
     </tr>
     <tr>
       <td class="tg-0pky">bifurcation</td>
       <td class="tg-c3ow">X</td>
       <td class="tg-c3ow"></td>
       <td class="tg-c3ow">X</td>
     </tr>
     <tr>
       <td class="tg-phtq">logi_branch_points</td>
       <td class="tg-svo0">X</td>
       <td class="tg-svo0"></td>
       <td class="tg-svo0"></td>
     </tr>
     <tr>
       <td class="tg-0pky">plot_logi_interact</td>
       <td class="tg-c3ow"></td>
       <td class="tg-c3ow"></td>
       <td class="tg-c3ow">X</td>
     </tr>
   </table>
   </br>
   </p>
   



.. automodule:: chaoseverywhere.logi.code_python
   :members:
