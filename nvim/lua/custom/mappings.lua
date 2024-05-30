local M = {}

M.general = {
  n = {
    ["<C-h>"] = { "<cmd> TmuxNavigatorLeft<CR>", "window left"},
    ["<C-l>"] = { "<cmd> TmuxNavigatorRight<CR>", "window right"},
    ["<C-j>"] = { "<cmd> TmuxNavigatorDown<CR>", "window Down"},
    ["<C-k>"] = { "<cmd> TmuxNavigatorUp<CR>", "window Up"},
  }
}

M.dap = {
  plugin = true,
  n = {
    ["<leader>db"] = { "<cmd> DapToggleBreakpoint <CR>" },
    ["<leader>dus"] = {
      function ()
        local widgets = require('dap.ui.widgets');
        local sidebar = widgets.sidebar(widgets.scopes);
        sidebar.open();
      end,
      "Open debugging sidebar"
    }
  }
}

M.crates = {
  plugin = true,
  n = {
    ["<leader>rcu"] = {
      function ()
        require('crates').upgrade_all_crates()
      end,
      "update crates"
    }
  }
}

M.dap_python = {
  plugin = true,
  n = {
    ["<leader>dpr"] = {
      function()
        require('dap-python').test_method()
      end
    }
  }
}

return M
